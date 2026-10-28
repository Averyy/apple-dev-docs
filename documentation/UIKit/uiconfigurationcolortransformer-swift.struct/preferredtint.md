# preferredTint

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A color transformer that returns the preferred system accent color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
static let preferredTint: UIConfigurationColorTransformer
```

## Discussion

This color transformer returns the original color on platforms without a system accent color, or when the system accent color is set to Multicolor. When the system accent color is set to any other color, this color transformer returns that system accent color.

## See Also

### Creating a color transformer
- [init((UIColor) -> UIColor)](./init%28_%29.md)
  Creates a color transformer with the specified closure.
- [static let grayscale: UIConfigurationColorTransformer](./grayscale.md)
  Creates a color transformer that generates a grayscale version of the color.
- [static let monochromeTint: UIConfigurationColorTransformer](./monochrometint.md)
  A color transformer that returns the color with a monochrome tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-swift.struct/preferredtint)*