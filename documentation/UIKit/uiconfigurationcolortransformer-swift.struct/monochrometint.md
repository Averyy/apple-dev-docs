# monochromeTint

**Framework**: UIKit  
**Kind**: property

A color transformer that returns the color with a monochrome tint.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static let monochromeTint: UIConfigurationColorTransformer
```

#### Discussion

Use this color transformer to deemphasize a tinted item. The tinted item remains monochrome regardless of the system accent color.

## See Also

- [init((UIColor) -> UIColor)](uiconfigurationcolortransformer-swift.struct/init(_:).md)
  Creates a color transformer with the specified closure.
- [static let grayscale: UIConfigurationColorTransformer](uiconfigurationcolortransformer-swift.struct/grayscale.md)
  Creates a color transformer that generates a grayscale version of the color.
- [static let preferredTint: UIConfigurationColorTransformer](uiconfigurationcolortransformer-swift.struct/preferredtint.md)
  A color transformer that returns the preferred system accent color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-swift.struct/monochrometint)*