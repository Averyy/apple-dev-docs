# CMSimpleQueueReset(_:)

**Framework**: Core Media  
**Kind**: func

Resets the queue.

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
func CMSimpleQueueReset(_ queue: CMSimpleQueue) -> OSStatus
```

#### Return Value

Returns `noErr` if the call succeeds.

#### Discussion

This function resets the queue to an empty state. `CMSimpleQueueReset` isn’t synchronized in any way, so the client must hold off the reader thread and writer thread during this operation.

## Parameters

- `queue`: The queue to reset. Must not be  .

## See Also

- [func CMSimpleQueueEnqueue(CMSimpleQueue, element: UnsafeRawPointer) -> OSStatus](cmsimplequeueenqueue(_:element:).md)
  Enqueues an element in the queue.
- [func CMSimpleQueueDequeue(CMSimpleQueue) -> UnsafeRawPointer?](cmsimplequeuedequeue(_:).md)
  Dequeues an element from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeuereset(_:))*