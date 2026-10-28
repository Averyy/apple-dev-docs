# smoothLinearGradient()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (CIFilter<CISmoothLinearGradient> *) smoothLinearGradientFilter;
```

## Return Value

The generated image.

## Discussion

This method generates a smooth linear-gradient image. The effect creates a gradient by gradually blending colors between `point0` and `point1` using the sigmoid curve function.

The smooth linear-gradient filter uses the following properties:

- **`point0`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) representing the starting position of the gradient.
- **`point1`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) representing the ending position of the gradient.
- **`color0`**: A [`CIColor`](../cicolor.md) representing the first color used in the gradient.
- **`color1`**: A [`CIColor`](../cicolor.md) representing the second color used in the gradient.

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

![An image that gradually changes in color from yellow in the bottom left corner to light blue in the top right corner.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3558802@2x.png)

## See Also

### Filters
- [class func gaussianGradient() -> any CIFilter & CIGaussianGradient](./gaussiangradient%28%29.md)
  Generates a gradient that varies from one color to another using a Gaussian distribution.
- [class func hueSaturationValueGradient() -> any CIFilter & CIHueSaturationValueGradient](./huesaturationvaluegradient%28%29.md)
  Generates a gradient representing a specified color space.
- [class func linearGradient() -> any CIFilter & CILinearGradient](./lineargradient%28%29.md)
  Generates a color gradient that varies along a linear axis between two defined endpoints.
- [class func radialGradient() -> any CIFilter & CIRadialGradient](./radialgradient%28%29.md)
  Generates a gradient that varies radially between two circles having the same center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/smoothlineargradient())*