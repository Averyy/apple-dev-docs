# system(_:design:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Gets a system font with the given text style and design.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`system(_:design:weight:)`](./system%28_,design,weight%29.md) instead.

## Declaration

```swift
static func system(_ style: Font.TextStyle, design: Font.Design = .default) -> Font
```

## See Also

### Getting system fonts
- [static func system(Font.TextStyle, design: Font.Design?, weight: Font.Weight?) -> Font](./system%28_,design,weight%29.md)
  Gets a system font that uses the specified style, design, and weight.
- [Font.Design](./design.md)
  A design to use for fonts.
- [Font.TextStyle](./textstyle.md)
  A dynamic text style to use for fonts.
- [struct Weight](./weight.md)
  A weight to use for fonts.
- [static func system(size: CGFloat, weight: Font.Weight?, design: Font.Design?) -> Font](./system%28size,weight,design%29-697b2.md)
  Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.
- [static func system(size: CGFloat, weight: Font.Weight, design: Font.Design) -> Font](./system%28size,weight,design%29-73a88.md)
  Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/system(_:design:))*