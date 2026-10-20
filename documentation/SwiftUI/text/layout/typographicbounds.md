# Text.Layout.TypographicBounds

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [init()](./typographicbounds/init%28%29.md)
  Initializes to an empty bounds with zero origin.
### Instance Properties
- [var ascent: CGFloat](./typographicbounds/ascent.md)
  The ascent of the element.
- [var descent: CGFloat](./typographicbounds/descent.md)
  The descent of the element.
- [var leading: CGFloat](./typographicbounds/leading.md)
  The leading of the element.
- [var origin: CGPoint](./typographicbounds/origin.md)
  The position of the left edge of the element’s baseline, relative to the text view.
- [var rect: CGRect](./typographicbounds/rect.md)
  Returns a rectangle encapsulating the bounds.
- [var width: CGFloat](./typographicbounds/width.md)
  The width of the element.

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Copyable](../../../Swift/copyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/layout/typographicbounds)*