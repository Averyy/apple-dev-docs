# Text.TruncationMode

**Framework**: SwiftUI  
**Kind**: enum

The type of truncation to apply to a line of text when it’s too long to fit in the available space.

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
enum TruncationMode
```

#### Overview

When a text view contains more text than it’s able to display, the view might truncate the text and place an ellipsis (…) at the truncation point. Use the [`truncationMode(_:)`](view/truncationmode(_:).md) modifier with one of the `TruncationMode` values to indicate which part of the text to truncate, either at the beginning, in the middle, or at the end.

## Topics

### Getting text truncation modes
- [Text.TruncationMode.head](text/truncationmode/head.md)
  Truncate at the beginning of the line.
- [Text.TruncationMode.middle](text/truncationmode/middle.md)
  Truncate in the middle of the line.
- [Text.TruncationMode.tail](text/truncationmode/tail.md)
  Truncate at the end of the line.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func textScale(Text.Scale, isEnabled: Bool) -> Text](text/textscale(_:isenabled:).md)
  Applies a text scale to the text.
- [struct Scale](text/scale.md)
  Defines text scales


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/truncationmode)*