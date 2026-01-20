# maskedVariableBlur()

**Framework**: Core Image  
**Kind**: method

Blurs a specified portion of an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func maskedVariableBlur() -> any CIFilter & CIMaskedVariableBlur
```

## Mentions

- [Selectively Focusing on an Image](selectively-focusing-on-an-image.md)

#### Return Value

The blurred image.

#### Discussion

This method applies the masked variable blur to an image. The effect blurs the image in an area defined by the mask image. The mask image contains shades of grey that define the strength of the blur. Black colors in the mask cause no blurring, and white colors cause maximum blur.

The masked variable blur filter uses the following properties:

The following code creates a filter that adds a blur to the bottom of the input image:

```swift
func maskedVariableBlur(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.maskedVariableBlur()
    filter.inputImage = inputImage
    // Create a mask that goes from white to black vertially.
    let mask = CIFilter.smoothLinearGradient()
    mask.color0 = CIColor.white
    mask.color1 = CIColor.black
    mask.point0 = CGPoint(x: 0, y: 0)
    mask.point1 = CGPoint(x:0, y: inputImage.extent.height)
    filter.mask = mask.outputImage
    filter.radius = 25
    return filter.outputImage!
}
```

![Three images, with two images on the left arranged vertically and a third image on the right vertically centered. The top left image contains a photo of the Golden Gate Bridge with a clear sky in the background. The bottom left image contains a white to black gradient with white at the bottom and black at the top. The right image shows the result of applying the masked variable blur filter using the two images on the left as inputs. The resulting image has a strong blur at the bottom that reduces to zero blur at the top.](https://docs-assets.developer.apple.com/published/56f6433d26ca41bc9abbf5a6d2a3256e/media-4334872%402x.png)

## See Also

- [class func bokehBlur() -> any CIFilter & CIBokehBlur](cifilter-swift.class/bokehblur.md)
  Applies a bokeh effect to an image.
- [class func boxBlur() -> any CIFilter & CIBoxBlur](cifilter-swift.class/boxblur.md)
  Applies a square-shaped blur to an area of an image.
- [class func discBlur() -> any CIFilter & CIDiscBlur](cifilter-swift.class/discblur.md)
  Applies a circle-shaped blur to an area of an image.
- [class func gaussianBlur() -> any CIFilter & CIGaussianBlur](cifilter-swift.class/gaussianblur.md)
  Blurs an image with a Gaussian distribution pattern.
- [class func median() -> any CIFilter & CIMedian](cifilter-swift.class/median.md)
  Calculates the median of an image to refine detail.
- [class func morphologyGradient() -> any CIFilter & CIMorphologyGradient](cifilter-swift.class/morphologygradient.md)
  Detects and highlights edges of objects.
- [class func morphologyMaximum() -> any CIFilter & CIMorphologyMaximum](cifilter-swift.class/morphologymaximum.md)
  Blurs a circular area by enlarging contrasting pixels.
- [class func morphologyMinimum() -> any CIFilter & CIMorphologyMinimum](cifilter-swift.class/morphologyminimum.md)
  Blurs a circular area by reducing contrasting pixels.
- [class func morphologyRectangleMaximum() -> any CIFilter & CIMorphologyRectangleMaximum](cifilter-swift.class/morphologyrectanglemaximum.md)
  Blurs a rectangular area by enlarging contrasting pixels.
- [class func morphologyRectangleMinimum() -> any CIFilter & CIMorphologyRectangleMinimum](cifilter-swift.class/morphologyrectangleminimum.md)
  Blurs a rectangular area by reducing contrasting pixels.
- [class func motionBlur() -> any CIFilter & CIMotionBlur](cifilter-swift.class/motionblur.md)
  Creates motion blur on an image.
- [class func noiseReduction() -> any CIFilter & CINoiseReduction](cifilter-swift.class/noisereduction.md)
  Reduces noise by sharpening the edges of objects.
- [class func zoomBlur() -> any CIFilter & CIZoomBlur](cifilter-swift.class/zoomblur.md)
  Creates a zoom blur centered around a single point on the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/maskedvariableblur())*