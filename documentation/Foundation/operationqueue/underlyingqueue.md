# underlyingQueue

**Framework**: Foundation  
**Kind**: property

The dispatch queue that the operation queue uses to invoke operations.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
unowned(unsafe) var underlyingQueue: dispatch_queue_t? { get set }
```

#### Discussion

The default value of this property is `nil`. You can set the value of this property to an existing dispatch queue to have enqueued operations interspersed with blocks submitted to that dispatch queue.

The value of this property should only be set if there are no operations in the queue; setting the value of this property when [`operationCount`](operationqueue/operationcount.md) is not equal to `0` raises an [`invalidArgumentException`](nsexceptionname/invalidargumentexception.md). The value of this property must not be the value returned by [`dispatch_get_main_queue`](https://developer.apple.com/documentation/dispatch/1452921-dispatch_get_main_queue). The quality-of-service level set for the underlying dispatch queue overrides any value set for the operation queue’s [`qualityOfService`](operationqueue/qualityofservice.md) property.

> **Note**:  This property automatically retains its assigned queue if `OS_OBJECT_IS_OBJC` is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var name: String?](operationqueue/name.md)
  The name of the operation queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/underlyingqueue)*