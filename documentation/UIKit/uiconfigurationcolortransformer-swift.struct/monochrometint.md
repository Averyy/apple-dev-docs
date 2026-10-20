# monochromeTint

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A color transformer that returns the color with a monochrome tint.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
static let monochromeTint: UIConfigurationColorTransformer
```

#### Discussion

Use this color transformer to deemphasize a tinted item. The tinted item remains monochrome regardless of the system accent color.

## See Also

### Creating a color transformer
- [init((UIColor) -> UIColor)](./init%28_%29.md)
  Creates a color transformer with the specified closure.
- [static let grayscale: UIConfigurationColorTransformer](./grayscale.md)
  Creates a color transformer that generates a grayscale version of the color.
- [static let preferredTint: UIConfigurationColorTransformer](./preferredtint.md)
  A color transformer that returns the preferred system accent color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-swift.struct/monochrometint)*