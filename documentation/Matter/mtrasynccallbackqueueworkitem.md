# MTRAsyncCallbackQueueWorkItem

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+ - Deprecated in 17.2
- iPadOS 16.1+ - Deprecated in 17.2
- Mac Catalyst 16.1+ - Deprecated in 17.2
- macOS 13.0+ - Deprecated in 14.2
- tvOS 16.1+ - Deprecated in 17.2
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 10.2

> **Deprecated**: This class was not intended to be part of the public Matter API

## Declaration

```swift
class MTRAsyncCallbackQueueWorkItem
```

```objc
@interface MTRAsyncCallbackQueueWorkItem : NSObject
```

## Topics

### Initializers
- [init(queue: dispatch_queue_t)](./mtrasynccallbackqueueworkitem/init%28queue%29.md)
### Instance Properties
- [var cancelHandler: () -> Void](./mtrasynccallbackqueueworkitem/cancelhandler.md)
- [var readyHandler: MTRAsyncCallbackReadyHandler](./mtrasynccallbackqueueworkitem/readyhandler.md)
### Instance Methods
- [func endWork()](./mtrasynccallbackqueueworkitem/endwork%28%29.md)
- [func retryWork()](./mtrasynccallbackqueueworkitem/retrywork%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrasynccallbackqueueworkitem)*