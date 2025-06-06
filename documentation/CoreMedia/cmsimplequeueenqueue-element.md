# CMSimpleQueueEnqueue(_:element:)

**Framework**: Core Media  
**Kind**: func

Enqueues an element in the queue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMSimpleQueueEnqueue(_ queue: CMSimpleQueue, element: UnsafeRawPointer) -> OSStatus
```

#### Return Value

Returns `noErr` if the call succeeds or `kCMSimpleQueueError_QueueIsFull` if the queue is full.

#### Discussion

If the queue is full, this operation fails.

## Parameters

- `queue`: The queue on which to enqueue the element. Must not be  .
- `element`: Element to enqueue. Must not be   (  returns   to indicate an empty queue).

## See Also

- [func CMSimpleQueueDequeue(CMSimpleQueue) -> UnsafeRawPointer?](cmsimplequeuedequeue(_:).md)
  Dequeues an element from the queue.
- [func CMSimpleQueueReset(CMSimpleQueue) -> OSStatus](cmsimplequeuereset(_:).md)
  Resets the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeueenqueue(_:element:))*