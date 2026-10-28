# gaussianGradient()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates a gradient that varies from one color to another using a Gaussian distribution.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func gaussianGradient() -> any CIFilter & CIGaussianGradient
```

```objc
+ (CIFilter<CIGaussianGradient> *) gaussianGradientFilter;
```

## Return Value

The generated image.

## Discussion

This method generates a Gaussian gradient image. The effect uses the Gaussian kernel to calculate the even dispersal of the first color in the center to the second color in the image’s periphery.

The Gaussian gradient filter uses the following properties:

- **`center`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) representing the center of the effect as x and y coordinates.
- **`color0`**: A [`CIColor`](../cicolor.md) representing the first color to use in the gradient.
- **`color1`**: A [`CIColor`](../cicolor.md) representing the second color to use in the gradient.
- **`radius`**: A `float` representing the radius of the Gaussian distribution as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that generates a gradient image:

```swift
func gaussian() -> CIImage {
    let gaussianGradient = CIFilter.gaussianGradient()
    gaussianGradient.center = CGPoint (x: 150, y: 150)
    gaussianGradient.color0 = CIColor(red: 88/255, green: 201
/255, blue: 175/255)
    gaussianGradient.color1 = CIColor(red: 153/255, green: 153/255, blue: 204/255)
    gaussianGradient.radius = 10
    return gaussianGradient.outputImage!
}
```

![A photo of a Gaussian gradient that gradually changes in color from purple in the center and shifts to light blue in the periphery.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3558795@2x.png)

## See Also

### Filters
- [class func hueSaturationValueGradient() -> any CIFilter & CIHueSaturationValueGradient](./huesaturationvaluegradient%28%29.md)
  Generates a gradient representing a specified color space.
- [class func linearGradient() -> any CIFilter & CILinearGradient](./lineargradient%28%29.md)
  Generates a color gradient that varies along a linear axis between two defined endpoints.
- [class func radialGradient() -> any CIFilter & CIRadialGradient](./radialgradient%28%29.md)
  Generates a gradient that varies radially between two circles having the same center.
- [class func smoothLinearGradient() -> any CIFilter & CISmoothLinearGradient](./smoothlineargradient%28%29.md)
  Generates a gradient that blends colors along a linear axis between two defined endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/gaussiangradient())*