# AttributedString.LineHeight

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

## Overview

The line height defines the distance between the baselines of two subsequent lines of text.

## Topics

### Type Properties
- [static var loose: AttributedString.LineHeight](./lineheight/loose.md)
  Constant line height based on a multiple of the point size that is perceived as loose.
- [static var normal: AttributedString.LineHeight](./lineheight/normal.md)
  Constant line height based on a multiple of the point size that is perceived as normal.
- [static var tight: AttributedString.LineHeight](./lineheight/tight.md)
  Constant line height based on a multiple of the point size that is perceived as tight.
- [static var variable: AttributedString.LineHeight](./lineheight/variable.md)
  Variable line height based on font metrics.
### Type Methods
- [static func exact(points: CGFloat) -> AttributedString.LineHeight](./lineheight/exact%28points%29.md)
  Constant line height based on a fixed total.
- [static func leading(increase: CGFloat) -> AttributedString.LineHeight](./lineheight/leading%28increase%29.md)
  Constant line height based on point size and a fixed increase.
- [static func multiple(factor: CGFloat) -> AttributedString.LineHeight](./lineheight/multiple%28factor%29.md)
  Constant line height based on a multiple of the point size.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/lineheight)*