# CMSimpleQueueEnqueue(_:element:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus CMSimpleQueueEnqueue(CMSimpleQueueRef queue, const void *element);
```

## Return Value

Returns `noErr` if the call succeeds or `kCMSimpleQueueError_QueueIsFull` if the queue is full.

## Discussion

If the queue is full, this operation fails.

## Parameters

- `queue`: The queue on which to enqueue the element. Must not be `NULL`.
- `element`: Element to enqueue. Must not be `NULL` (`CMSimpleQueueDequeue` returns `NULL` to indicate an empty queue).

## See Also

### Managing Queues
- [func CMSimpleQueueDequeue(CMSimpleQueue) -> UnsafeRawPointer?](./cmsimplequeuedequeue%28_%29.md)
  Dequeues an element from the queue.
- [func CMSimpleQueueReset(CMSimpleQueue) -> OSStatus](./cmsimplequeuereset%28_%29.md)
  Resets the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeueenqueue(_:element:))*