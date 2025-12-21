# AttributedString.LineHeight

**Framework**: Foundation  
**Kind**: struct

The line height definition of a paragraph.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct LineHeight
```

#### Overview

The line height defines the distance between the baselines of two subsequent lines of text.

## Topics

### Type Properties
- [static var loose: AttributedString.LineHeight](attributedstring/lineheight/loose.md)
  Constant line height based on a multiple of the point size that is perceived as loose.
- [static var normal: AttributedString.LineHeight](attributedstring/lineheight/normal.md)
  Constant line height based on a multiple of the point size that is perceived as normal.
- [static var tight: AttributedString.LineHeight](attributedstring/lineheight/tight.md)
  Constant line height based on a multiple of the point size that is perceived as tight.
- [static var variable: AttributedString.LineHeight](attributedstring/lineheight/variable.md)
  Variable line height based on font metrics.
### Type Methods
- [static func exact(points: CGFloat) -> AttributedString.LineHeight](attributedstring/lineheight/exact(points:).md)
  Constant line height based on a fixed total.
- [static func leading(increase: CGFloat) -> AttributedString.LineHeight](attributedstring/lineheight/leading(increase:).md)
  Constant line height based on point size and a fixed increase.
- [static func multiple(factor: CGFloat) -> AttributedString.LineHeight](attributedstring/lineheight/multiple(factor:).md)
  Constant line height based on a multiple of the point size.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/lineheight)*