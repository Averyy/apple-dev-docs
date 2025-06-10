# Font.Design

**Framework**: SwiftUI  
**Kind**: enum

A design to use for fonts.

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
enum Design
```

## Topics

### Getting font designs
- [Font.Design.default](font/design/default.md)
- [Font.Design.monospaced](font/design/monospaced.md)
- [Font.Design.rounded](font/design/rounded.md)
- [Font.Design.serif](font/design/serif.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func system(Font.TextStyle, design: Font.Design?, weight: Font.Weight?) -> Font](font/system(_:design:weight:).md)
  Gets a system font that uses the specified style, design, and weight.
- [static func system(size: CGFloat, weight: Font.Weight?, design: Font.Design?) -> Font](font/system(size:weight:design:)-697b2.md)
  Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.
- [Font.TextStyle](font/textstyle.md)
  A dynamic text style to use for fonts.
- [struct Weight](font/weight.md)
  A weight to use for fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/design)*