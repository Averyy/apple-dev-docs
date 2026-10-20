# Text.LineStyle.Pattern

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The pattern, that the line has.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Pattern
```

## Topics

### Getting line style patterns
- [static let solid: Text.LineStyle.Pattern](./pattern/solid.md)
  Draw a solid line.
- [static let dot: Text.LineStyle.Pattern](./pattern/dot.md)
  Draw a line of dots.
- [static let dash: Text.LineStyle.Pattern](./pattern/dash.md)
  Draw a line of dashes.
- [static let dashDot: Text.LineStyle.Pattern](./pattern/dashdot.md)
- [static let dashDotDot: Text.LineStyle.Pattern](./pattern/dashdotdot.md)
  Draw a line of alternating dashes and two dots.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating a text line style
- [init?(nsUnderlineStyle: NSUnderlineStyle)](./init%28nsunderlinestyle%29.md)
  Creates a `Text.LineStyle` from `NSUnderlineStyle`.
- [init(pattern: Text.LineStyle.Pattern, color: Color?)](./init%28pattern,color%29.md)
  Creates a line style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/linestyle/pattern)*