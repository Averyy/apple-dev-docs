# Applying tone curve adjustments to images

**Framework**: Accelerate

Use the vImage library’s polynomial transform to apply tone curve adjustments to images.

**Availability**:
- macOS 13.3+
- Xcode 15.0+

#### Overview

The vImage library provides a suite of functions for applying polynomials to images. The results of these functions are similar to the [`Curves adjustment`](https://developer.apple.comhttps://support.apple.com/en-gb/guide/photos/pht7875d6b19/7.0/mac/12.0) tool in the [`Mac Photos`](https://developer.apple.comhttps://www.apple.com/uk/macos/photos/) app. You can use the polynomial adjustment functions to adjust the overall look of a photo, change the look of specific colors (red, green, and blue), and adjust settings for the black point, midtones, and white point.

This sample code project calculates the polynomial coefficients from a set of values that the user defines using handles in the user interface. The vImage polynomial functions evaluate the polynomial coefficients to define the tone curve. The technique that calculates the coefficients is the Vandermonde method. To learn more about this technique, see [`Finding an interpolating polynomial using the Vandermonde method`](finding-an-interpolating-polynomial-using-the-vandermonde-method.md).

To generate the smooth curves in the user interface, the app passes the same coefficients that the vImage polynomial transform function uses to the vDSP [`evaluatePolynomial(usingCoefficients:withVariables:)`](vdsp/evaluatepolynomial(usingcoefficients:withvariables:)-31vi2.md) function.

The following image shows the sample code project’s app. The circles on the curves are the handles that the user can drag vertically, and the image changes to show the effect of the polynomial transform.

![A screenshot showing the sample code app with the transformed photograph on the left after adjustment, and the three tone curve controls on the right for the red, green, and blue channels.](https://docs-assets.developer.apple.com/published/dc8351ac3a9e7073974d9decfac88e97/vImagePolynomial_2x.png)

##### Convert the Interleaved Source Image to Planar Buffers

The sample code project accepts source images that it converts to RGB, 32-bit per channel format. Because the vImage polynomial transform functions work on planar buffers, the code creates a [`vImage.PlanarFx3`](vimage/planarfx3.md) multiple-plane [`vImage.PixelBuffer`](vimage/pixelbuffer.md) structure that contains the separate red, green, and blue channels.

After creating [`vImage.PixelBuffer`](vimage/pixelbuffer.md) structures that store the interleaved and planar representations of the source image, the `populatePlanarSourceBuffers()` function copies and deinterleaves the interleaved image to the planar buffers.

```swift
func populatePlanarSourceBuffers() {
    srcInterleavedBuffer.deinterleave(destination: srcPlanarBuffers)
}
```

To learn more about working with planar buffers in vImage, see [`Optimizing image-processing performance`](optimizing-image-processing-performance.md).

##### Create the Default Curve Control Points

The sample code project defines five data points for each color channel that control the tone curve. By default, these form a linear ramp from `0` to `1`. The code calls [`ramp(withInitialValue:increment:count:)`](vdsp/ramp(withinitialvalue:increment:count:)-3cast.md) to populate the `redHandleValues`, `greenHandleValues`, and `blueHandleValues` arrays. The following shows the code that populates the `greenHandleValues` array:

```swift
greenHandleValues = vDSP.ramp(
    in: 0 ... 1,
    count: PolynomialTransformer.count)
```

When the sample code app first launches, the default values form a linear tone curve that renders as a stright line in the user interface.

![A screenshot showing the sample code app with the original unadjusted photograph on the left, and the three linear tone controls on the right for the red, green, and blue channels.](https://docs-assets.developer.apple.com/published/be0076c7c847f81d910518064d785e2a/tone_curve.png)

The default control points create an output image that’s identical to the input image. That is, for each pixel, the transformed output value is equal to the input value.

##### Apply the Polynomial Transform

When the user adjusts the control points in the user interface, a `didSet` property observer applies the polynomial to the corresponding planar buffer. For example, the following shows the code for the green values:

```swift
@Published var greenHandleValues: [Double]! {
    didSet {
        greenCoefficients = calculateAndApplyPolynomial(
            forHandleValues: greenHandleValues,
            at: 1,
            source: srcPlanarBuffers,
            destination: destPlanarBuffers)
        
        displayPlanarDestinationBuffers()
    }
}
```

The `calculateAndApplyPolynomial()` function calls `calculateCoefficients()` to calculate the coefficients using the Vandermonde method. It then passes the coefficients to [`applyPolynomial(coefficientSegments:boundaries:destination:)`](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-26zom.md). The vImage polynomial function effectively creates a polynomial curve from the specified coefficients and uses that as the tone curve. For each point on the curve, the horizontal position represents the input value, and the vertical position represents the output value.

```swift
func calculateAndApplyPolynomial(
    forHandleValues values: [Double],
    at planeIndex: Int,
    source: vImage.PixelBuffer<vImage.PlanarFx4>,
    destination: vImage.PixelBuffer<vImage.PlanarFx4>) -> [Float] {
        
        let coefficients = calculateCoefficients(values: values.map { Float($0) })
        
        source.withUnsafePixelBuffer(at: planeIndex) { src in
            destination.withUnsafePixelBuffer(at: planeIndex) { dest in
                
                src.applyPolynomial(
                    coefficientSegments: [coefficients],
                    boundaries: [-.infinity, .infinity],
                    destination: dest)
            }
        }
        
        return coefficients
    }
```

After the transform, the `displayPlanarDestinationBuffers()` function calls [`interleave(destination:)`](vimage/pixelbuffer/interleave(destination:)-46cgi.md) to generate an interleaved image that the sample code displays in the user interface.

##### Display the Tone Curve in the User Interface

The `PolynomialEditor` class uses the coefficients that the `applyPolynomial()` function computes to render a representation of the response curve.

The `updatePath()` function calls [`evaluatePolynomial(usingCoefficients:withVariables:result:)`](vdsp/evaluatepolynomial(usingcoefficients:withvariables:result:)-2ncdh.md) to build a [`CGPath`](https://developer.apple.com/documentation/CoreGraphics/CGPath) instance that the editor uses to render a smooth curve in the user interface.

```swift
static func updatePath(path: inout Path,
                       size: CGSize,
                       coefficients: [Float]) {
    
    let polynomialResult = [Float](unsafeUninitializedCapacity: ramp.count) {
        buffer, initializedCount in
        
        vDSP.evaluatePolynomial(usingCoefficients: coefficients.reversed(),
                                withVariables: ramp,
                                result: &buffer)
        
        vDSP.clip(buffer,
                  to: 0 ... 1,
                  result: &buffer)
        
        initializedCount = ramp.count
    }

    let cgPath = CGMutablePath()
    let hScale = size.width / 256
    let points: [CGPoint] = polynomialResult.enumerated().map {
        CGPoint(x: CGFloat($0.offset) * hScale,
                y: size.height - (size.height * CGFloat($0.element) ))
    }

    cgPath.addLines(between: points)
    
    path = Path(cgPath)
}
```

## See Also

- [Adjusting the brightness and contrast of an image](adjusting-the-brightness-and-contrast-of-an-image.md)
  Use a gamma function to apply a linear or exponential curve.
- [Adjusting saturation and applying tone mapping](adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.
- [Adjusting the hue of an image](adjusting-the-hue-of-an-image.md)
  Convert an image to L*a*b* color space and apply hue adjustment.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Histogram](histogram.md)
  Calculate or manipulate an image’s histogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-tone-curve-adjustments-to-images)*