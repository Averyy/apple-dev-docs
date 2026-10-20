# NSTouchBarItem.Priority

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

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

```c
typedef float NSTouchBarItemPriority;
```

#### Discussion

Use these constants to set the [`visibilityPriority`](./visibilitypriority.md) property of an [`NSTouchBarItem`](../nstouchbaritem.md) instance. The Touch Bar hides items of lower priority when there isn’t enough space to show all items.

## Topics

### Priorities
- [static var low: NSTouchBarItem.Priority](./priority/low.md)
  A constant indicating a low visibility priority.
- [static var normal: NSTouchBarItem.Priority](./priority/normal.md)
  A constant indicating a normal visibility priority.
- [static var high: NSTouchBarItem.Priority](./priority/high.md)
  A constant indicating a high visibility priority.
### Initializers
- [init(Float)](./priority/init%28_%29.md)
  Creates a new priority structure from the given value.
- [init(rawValue: Float)](./priority/init%28rawvalue%29.md)
  Creates a new priority structure from the given raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Comparable](../../Swift/comparable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing item visibility
- [var visibilityPriority: NSTouchBarItem.Priority](./visibilitypriority.md)
  Determines which items are shown in a bar when space is limited.
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that reflects whether or not the item is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem/priority)*