# CMSimpleQueueDequeue(_:)

**Framework**: Core Media  
**Kind**: func

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

#### Return Value

The dequeued element.  `NULL` if the queue was empty, or if there was some other error.

## Parameters

- `queue`: The queue from which to dequeue an element. Must not be  .

## See Also

- [func CMSimpleQueueEnqueue(CMSimpleQueue, element: UnsafeRawPointer) -> OSStatus](cmsimplequeueenqueue(_:element:).md)
  Enqueues an element in the queue.
- [func CMSimpleQueueReset(CMSimpleQueue) -> OSStatus](cmsimplequeuereset(_:).md)
  Resets the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeuedequeue(_:))*