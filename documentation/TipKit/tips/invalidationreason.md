# InvalidationReason

**Framework**: TipKit  
**Kind**: enum

A type that describes why the system permanently invalidated a tip.

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
enum InvalidationReason
```

## Topics

### Enumeration Cases
- [Tips.InvalidationReason.actionPerformed](tips/invalidationreason/actionperformed.md)
  The user performed the action that the tip describes.
- [Tips.InvalidationReason.displayCountExceeded](tips/invalidationreason/displaycountexceeded.md)
  The tip exceeded its maximum display count.
- [Tips.InvalidationReason.displayDurationExceeded](tips/invalidationreason/displaydurationexceeded.md)
  The tip exceeded its max display duration.
- [Tips.InvalidationReason.tipClosed](tips/invalidationreason/tipclosed.md)
  The user explicitly closed the tip view while it was displaying.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum Status](tips/status.md)
  A type that describes the current display eligibility status for a tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/invalidationreason)*