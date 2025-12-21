# NEURLFilterManager.Status

**Framework**: Network Extension  
**Kind**: enum

An enumeration of URL filter status codes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum Status
```

## Topics

### URL filter statuses
- [NEURLFilterManager.Status.invalid](neurlfiltermanager/status-swift.enum/invalid.md)
  The URL filter isn’t configured.
- [NEURLFilterManager.Status.stopped](neurlfiltermanager/status-swift.enum/stopped.md)
  The URL filter is stopped.
- [NEURLFilterManager.Status.starting](neurlfiltermanager/status-swift.enum/starting.md)
  The URL filter is starting.
- [NEURLFilterManager.Status.running](neurlfiltermanager/status-swift.enum/running.md)
  The URL filter is running.
- [NEURLFilterManager.Status.stopping](neurlfiltermanager/status-swift.enum/stopping.md)
  The URL filter is stopping.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var status: NEURLFilterManager.Status](neurlfiltermanager/status-swift.property.md)
  The current status of the URL filter.
- [func handleStatusChange() -> any AsyncSequence<NEURLFilterManager.Status, Never>](neurlfiltermanager/handlestatuschange.md)
  Sets up an observer for the status notification and models it as an asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/status-swift.enum)*