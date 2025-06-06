# name

**Framework**: Foundation  
**Kind**: property

The name of the operation queue.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String? { get set }
```

#### Discussion

Names provide a way for you to identify your operation queues at run time. Tools may also use this name to provide additional context during debugging or analysis of your code.

The default value of this property is a string containing the memory address of the operation queue. You may monitor changes to the value of this property using [`Key-value observing`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16). Configure an observer to monitor the [`name`](operationqueue/name.md) key path of the operation queue.

## See Also

- [var underlyingQueue: dispatch_queue_t?](operationqueue/underlyingqueue.md)
  The dispatch queue that the operation queue uses to invoke operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/name)*