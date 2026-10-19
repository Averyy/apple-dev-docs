# system(_:design:)

**Framework**: SwiftUI  
**Kind**: method

Gets a system font with the given text style and design.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func system(_ style: Font.TextStyle, design: Font.Design = .default) -> Font
```

## See Also

- [static func system(Font.TextStyle, design: Font.Design?, weight: Font.Weight?) -> Font](font/system(_:design:weight:).md)
  Gets a system font that uses the specified style, design, and weight.
- [Font.Design](font/design.md)
  A design to use for fonts.
- [Font.TextStyle](font/textstyle.md)
  A dynamic text style to use for fonts.
- [struct Weight](font/weight.md)
  A weight to use for fonts.
- [static func system(size: CGFloat, weight: Font.Weight?, design: Font.Design?) -> Font](font/system(size:weight:design:)-697b2.md)
  Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.
- [static func system(size: CGFloat, weight: Font.Weight, design: Font.Design) -> Font](font/system(size:weight:design:)-73a88.md)
  Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/system(_:design:))*