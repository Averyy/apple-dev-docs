# TipGroup.Priority

**Framework**: TipKit  
**Kind**: enum  
**Role**: Enumeration

Order priority for a [`TipGroup`](../tipgroup.md).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum Priority
```

## Topics

### Enumeration Cases
- [TipGroup.Priority.firstAvailable](./priority/firstavailable.md)
  Shows the first tip eligible for display.
- [TipGroup.Priority.ordered](./priority/ordered.md)
  Shows an eligible tip when all of the previous tips have been [`invalidated`](../tips/status/invalidated%28_%29.md).

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipgroup/priority)*