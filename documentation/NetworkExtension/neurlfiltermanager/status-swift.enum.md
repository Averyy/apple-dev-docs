# NEURLFilterManager.Status

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

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
- [NEURLFilterManager.Status.invalid](./status-swift.enum/invalid.md)
  The URL filter isn’t configured.
- [NEURLFilterManager.Status.stopped](./status-swift.enum/stopped.md)
  The URL filter is stopped.
- [NEURLFilterManager.Status.starting](./status-swift.enum/starting.md)
  The URL filter is starting.
- [NEURLFilterManager.Status.running](./status-swift.enum/running.md)
  The URL filter is running.
- [NEURLFilterManager.Status.stopping](./status-swift.enum/stopping.md)
  The URL filter is stopping.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with filter statuses
- [var status: NEURLFilterManager.Status](./status-swift.property.md)
  The current status of the URL filter.
- [func handleStatusChange() -> any AsyncSequence<NEURLFilterManager.Status, Never>](./handlestatuschange%28%29.md)
  Sets up an observer for the status notification and models it as an asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/status-swift.enum)*