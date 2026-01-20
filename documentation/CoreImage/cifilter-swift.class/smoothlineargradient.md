# smoothLinearGradient()

**Framework**: Core Image  
**Kind**: method

Generates a gradient that blends colors along a linear axis between two defined endpoints.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func smoothLinearGradient() -> any CIFilter & CISmoothLinearGradient
```

#### Return Value

The generated image.

#### Discussion

This method generates a smooth linear-gradient image. The effect creates a gradient by gradually blending colors between `point0` and `point1` using the sigmoid curve function.

The smooth linear-gradient filter uses the following properties:

The following code creates a filter that generates a gradient image:

```swift
func smoothLinear() -> CIImage {
    let smoothLinearGradient = CIFilter.smoothLinearGradient()
    smoothLinearGradient.point0 = CGPoint(x: 0, y: 0)
    smoothLinearGradient.point1 = CGPoint(x: 200, y: 200)
    smoothLinearGradient.color0 = CIColor(red: 0/255, green: 112/255, blue: 201/255)
    smoothLinearGradient.color1 = CIColor(red: 216/255, green: 232/255, blue: 146/255)
    return smoothLinearGradient.outputImage!
}
```

![An image that gradually changes in color from yellow in the bottom left corner to light blue in the top right corner.](https://docs-assets.developer.apple.com/published/03ab63a8892b985c3ac8d0a7693deeed/media-3558802%402x.png)

## See Also

- [class func gaussianGradient() -> any CIFilter & CIGaussianGradient](cifilter-swift.class/gaussiangradient.md)
  Generates a gradient that varies from one color to another using a Gaussian distribution.
- [class func hueSaturationValueGradient() -> any CIFilter & CIHueSaturationValueGradient](cifilter-swift.class/huesaturationvaluegradient.md)
  Generates a gradient representing a specified color space.
- [class func linearGradient() -> any CIFilter & CILinearGradient](cifilter-swift.class/lineargradient.md)
  Generates a color gradient that varies along a linear axis between two defined endpoints.
- [class func radialGradient() -> any CIFilter & CIRadialGradient](cifilter-swift.class/radialgradient.md)
  Generates a gradient that varies radially between two circles having the same center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/smoothlineargradient())*