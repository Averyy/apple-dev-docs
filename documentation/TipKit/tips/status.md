# Status

**Framework**: TipKit  
**Kind**: enum

A type that describes the current display eligibility status for a tip.

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
enum Status
```

## Topics

### Enumeration Cases
- [Tips.Status.available](tips/status/available.md)
  The tip is eligible for display.
- [case invalidated(Tips.InvalidationReason)](tips/status/invalidated(_:).md)
  The tip is no longer valid.
- [Tips.Status.pending](tips/status/pending.md)
  The tip is not eligible for display.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum InvalidationReason](tips/invalidationreason.md)
  A type that describes why the system permanently invalidated a tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/status)*