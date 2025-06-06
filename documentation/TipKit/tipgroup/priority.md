# TipGroup.Priority

**Framework**: TipKit  
**Kind**: enum

Order priority for a [`TipGroup`](tipgroup.md).

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
- [TipGroup.Priority.firstAvailable](tipgroup/priority/firstavailable.md)
  Shows the first tip eligible for display.
- [TipGroup.Priority.ordered](tipgroup/priority/ordered.md)
  Shows an eligible tip when all of the previous tips have been [`Tips.Status.invalidated(_:)`](tips/status/invalidated(_:).md).

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipgroup/priority)*