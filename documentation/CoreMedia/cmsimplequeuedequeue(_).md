# CMSimpleQueueDequeue(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Dequeues an element from the queue.

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
func CMSimpleQueueDequeue(_ queue: CMSimpleQueue) -> UnsafeRawPointer?
```

```c
extern const void *CMSimpleQueueDequeue(CMSimpleQueueRef queue);
```

## Return Value

The dequeued element.  `NULL` if the queue was empty, or if there was some other error.

## Parameters

- `queue`: The queue from which to dequeue an element. Must not be `NULL`.

## See Also

### Managing Queues
- [func CMSimpleQueueEnqueue(CMSimpleQueue, element: UnsafeRawPointer) -> OSStatus](./cmsimplequeueenqueue%28_,element%29.md)
  Enqueues an element in the queue.
- [func CMSimpleQueueReset(CMSimpleQueue) -> OSStatus](./cmsimplequeuereset%28_%29.md)
  Resets the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeuedequeue(_:))*