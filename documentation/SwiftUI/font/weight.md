# Font.Weight

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A weight to use for fonts.

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
@frozen
struct Weight
```

## Topics

### Getting font weights
- [static let black: Font.Weight](./weight/black.md)
- [static let bold: Font.Weight](./weight/bold.md)
- [static let heavy: Font.Weight](./weight/heavy.md)
- [static let light: Font.Weight](./weight/light.md)
- [static let medium: Font.Weight](./weight/medium.md)
- [static let regular: Font.Weight](./weight/regular.md)
- [static let semibold: Font.Weight](./weight/semibold.md)
- [static let thin: Font.Weight](./weight/thin.md)
- [static let ultraLight: Font.Weight](./weight/ultralight.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting system fonts
- [static func system(Font.TextStyle, design: Font.Design?, weight: Font.Weight?) -> Font](./system%28_,design,weight%29.md)
  Gets a system font that uses the specified style, design, and weight.
- [Font.Design](./design.md)
  A design to use for fonts.
- [Font.TextStyle](./textstyle.md)
  A dynamic text style to use for fonts.
- [static func system(size: CGFloat, weight: Font.Weight?, design: Font.Design?) -> Font](./system%28size,weight,design%29-697b2.md)
  Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.
- [static func system(Font.TextStyle, design: Font.Design) -> Font](./system%28_,design%29.md)
  Gets a system font with the given text style and design.
- [static func system(size: CGFloat, weight: Font.Weight, design: Font.Design) -> Font](./system%28size,weight,design%29-73a88.md)
  Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/weight)*