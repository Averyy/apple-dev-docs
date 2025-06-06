# MTRAsyncCallbackQueueWorkItem

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRAsyncCallbackQueueWorkItem
```

## Topics

### Initializers
- [init(queue: dispatch_queue_t)](mtrasynccallbackqueueworkitem/init(queue:).md)
### Instance Properties
- [var cancelHandler: () -> Void](mtrasynccallbackqueueworkitem/cancelhandler.md)
- [var readyHandler: MTRAsyncCallbackReadyHandler](mtrasynccallbackqueueworkitem/readyhandler.md)
### Instance Methods
- [func endWork()](mtrasynccallbackqueueworkitem/endwork.md)
- [func retryWork()](mtrasynccallbackqueueworkitem/retrywork.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrasynccallbackqueueworkitem)*