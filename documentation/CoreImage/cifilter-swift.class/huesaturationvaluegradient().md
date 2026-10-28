# hueSaturationValueGradient()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates a gradient representing a specified color space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func hueSaturationValueGradient() -> any CIFilter & CIHueSaturationValueGradient
```

```objc
+ (CIFilter<CIHueSaturationValueGradient> *) hueSaturationValueGradientFilter;
```

## Return Value

The generated image.

## Discussion

This method generates a hue-saturation-value gradient image. The filter creates a color wheel that shows the hues and saturations for a specified [`CGColorSpace`](../../CoreGraphics/cgcolorspace.md).

The hue-saturation-value gradient uses the following properties:

- **`colorSpace`**: A [`CGColorSpace`](../../CoreGraphics/cgcolorspace.md) representing the color space for the generated color wheel.
- **`dither`**: A `boolean` value specifying whether the distort the generated output.
- **`radius`**: A `float` representing the distance from the center of the effect as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`softness`**: A `float` representing the softness of the generated color wheel as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`value`**: A `float` representing the lightness of the hue-saturation gradient as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that generates a color-space image:

```swift
func hueSaturationValue() -> CIImage {
    let hueSaturationValueGradient = CIFilter.hueSaturationValueGradient()
    hueSaturationValueGradient.colorSpace = CGColorSpaceCreateDeviceRGB()
    hueSaturationValueGradient.dither = 1
    hueSaturationValueGradient.radius = 100
    hueSaturationValueGradient.softness = 2
    hueSaturationValueGradient.value = 1
    return hueSaturationValueGradient.outputImage!
}
```

![A circular image containing every color in the represented colorspace.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3558798@2x.png)

## See Also

### Filters
- [class func gaussianGradient() -> any CIFilter & CIGaussianGradient](./gaussiangradient%28%29.md)
  Generates a gradient that varies from one color to another using a Gaussian distribution.
- [class func linearGradient() -> any CIFilter & CILinearGradient](./lineargradient%28%29.md)
  Generates a color gradient that varies along a linear axis between two defined endpoints.
- [class func radialGradient() -> any CIFilter & CIRadialGradient](./radialgradient%28%29.md)
  Generates a gradient that varies radially between two circles having the same center.
- [class func smoothLinearGradient() -> any CIFilter & CISmoothLinearGradient](./smoothlineargradient%28%29.md)
  Generates a gradient that blends colors along a linear axis between two defined endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/huesaturationvaluegradient())*