# preferredTint

**Framework**: UIKit  
**Kind**: property

A color transformer that returns the preferred system accent color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static let preferredTint: UIConfigurationColorTransformer
```

#### Discussion

This color transformer returns the original color on platforms without a system accent color, or when the system accent color is set to Multicolor. When the system accent color is set to any other color, this color transformer returns that system accent color.

## See Also

- [init((UIColor) -> UIColor)](uiconfigurationcolortransformer-swift.struct/init(_:).md)
  Creates a color transformer with the specified closure.
- [static let grayscale: UIConfigurationColorTransformer](uiconfigurationcolortransformer-swift.struct/grayscale.md)
  Creates a color transformer that generates a grayscale version of the color.
- [static let monochromeTint: UIConfigurationColorTransformer](uiconfigurationcolortransformer-swift.struct/monochrometint.md)
  A color transformer that returns the color with a monochrome tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-swift.struct/preferredtint)*