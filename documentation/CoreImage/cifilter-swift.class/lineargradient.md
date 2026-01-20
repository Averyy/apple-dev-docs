# linearGradient()

**Framework**: Core Image  
**Kind**: method

Generates a color gradient that varies along a linear axis between two defined endpoints.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func linearGradient() -> any CIFilter & CILinearGradient
```

## Mentions

- [Selectively Focusing on an Image](selectively-focusing-on-an-image.md)

#### Return Value

The generated image.

#### Discussion

This method generates a linear-gradient image. The effect creates a gradient that varies linearly between the two input properties of `point0` and `point1`.

The linear-gradient filter uses the following properties:

The following code creates a filter that generates a gradient image:

```swift
func linear() -> CIImage {
    let linearGradient = CIFilter.linearGradient()
    linearGradient.point0 = CGPoint(x: 0, y: 0)
    linearGradient.point1 = CGPoint(x: 200, y: 200)
    linearGradient.color0 = CIColor(red: 216/255, green: 232/255, blue: 146/255)
    linearGradient.color1 = CIColor(red: 0/255, green: 112/255, blue: 201/255)
    return linearGradient.outputImage!
}
```

![An image that gradually changes in color from yellow in the top left corner to light blue in the bottom right corner.](https://docs-assets.developer.apple.com/published/155a7d8d488e90f4d2f7a4a99d67f1ec/media-3558797%402x.png)

## See Also

- [class func gaussianGradient() -> any CIFilter & CIGaussianGradient](cifilter-swift.class/gaussiangradient.md)
  Generates a gradient that varies from one color to another using a Gaussian distribution.
- [class func hueSaturationValueGradient() -> any CIFilter & CIHueSaturationValueGradient](cifilter-swift.class/huesaturationvaluegradient.md)
  Generates a gradient representing a specified color space.
- [class func radialGradient() -> any CIFilter & CIRadialGradient](cifilter-swift.class/radialgradient.md)
  Generates a gradient that varies radially between two circles having the same center.
- [class func smoothLinearGradient() -> any CIFilter & CISmoothLinearGradient](cifilter-swift.class/smoothlineargradient.md)
  Generates a gradient that blends colors along a linear axis between two defined endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/lineargradient())*