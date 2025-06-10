# NSTouchBarItem.Priority

**Framework**: AppKit  
**Kind**: struct

Priorities for the visibility of a Touch Bar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
struct Priority
```

#### Discussion

Use these constants to set the [`visibilityPriority`](nstouchbaritem/visibilitypriority.md) property of an [`NSTouchBarItem`](nstouchbaritem.md) instance. The Touch Bar hides items of lower priority when there isn’t enough space to show all items.

## Topics

### Priorities
- [static let low: NSTouchBarItem.Priority](nstouchbaritem/priority/low.md)
  A constant indicating a low visibility priority.
- [static let normal: NSTouchBarItem.Priority](nstouchbaritem/priority/normal.md)
  A constant indicating a normal visibility priority.
- [static let high: NSTouchBarItem.Priority](nstouchbaritem/priority/high.md)
  A constant indicating a high visibility priority.
### Initializers
- [init(Float)](nstouchbaritem/priority/init(_:).md)
  Creates a new priority structure from the given value.
- [init(rawValue: Float)](nstouchbaritem/priority/init(rawvalue:).md)
  Creates a new priority structure from the given raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var visibilityPriority: NSTouchBarItem.Priority](nstouchbaritem/visibilitypriority.md)
  Determines which items are shown in a bar when space is limited.
- [var isVisible: Bool](nstouchbaritem/isvisible.md)
  A Boolean value that reflects whether or not the item is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem/priority)*