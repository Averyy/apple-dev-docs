# init(_:)

**Framework**: UIKit  
**Kind**: init

Creates a color transformer with the specified closure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
init(_ transform: @escaping (UIColor) -> UIColor)
```

## See Also

- [static let grayscale: UIConfigurationColorTransformer](uiconfigurationcolortransformer-swift.struct/grayscale.md)
  Creates a color transformer that generates a grayscale version of the color.
- [static let preferredTint: UIConfigurationColorTransformer](uiconfigurationcolortransformer-swift.struct/preferredtint.md)
  A color transformer that returns the preferred system accent color.
- [static let monochromeTint: UIConfigurationColorTransformer](uiconfigurationcolortransformer-swift.struct/monochrometint.md)
  A color transformer that returns the color with a monochrome tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-swift.struct/init(_:))*