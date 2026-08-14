# Text.Layout.TypographicBounds

**Framework**: SwiftUI  
**Kind**: struct

The typographic bounds of an element in a text layout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@frozen
struct TypographicBounds
```

## Topics

### Initializers
- [init()](text/layout/typographicbounds/init.md)
  Initializes to an empty bounds with zero origin.
### Instance Properties
- [var ascent: CGFloat](text/layout/typographicbounds/ascent.md)
  The ascent of the element.
- [var descent: CGFloat](text/layout/typographicbounds/descent.md)
  The descent of the element.
- [var leading: CGFloat](text/layout/typographicbounds/leading.md)
  The leading of the element.
- [var origin: CGPoint](text/layout/typographicbounds/origin.md)
  The position of the left edge of the element’s baseline, relative to the text view.
- [var rect: CGRect](text/layout/typographicbounds/rect.md)
  Returns a rectangle encapsulating the bounds.
- [var width: CGFloat](text/layout/typographicbounds/width.md)
  The width of the element.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/layout/typographicbounds)*