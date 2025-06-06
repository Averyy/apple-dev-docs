# CMSimpleQueueGetHead(_:)

**Framework**: Core Media  
**Kind**: func

Returns the element at the head of the queue.

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
func CMSimpleQueueGetHead(_ queue: CMSimpleQueue) -> UnsafeRawPointer?
```

#### Return Value

The head element.  `NULL` if the queue was empty, or if there was some other error.

#### Discussion

If the queue is empty, the function returns `NULL`.

## Parameters

- `queue`: The queue from which to get the head element. Must not be  .

## See Also

- [func CMSimpleQueueGetCapacity(CMSimpleQueue) -> Int32](cmsimplequeuegetcapacity(_:).md)
  Returns the number of elements that the queue can hold.
- [func CMSimpleQueueGetCount(CMSimpleQueue) -> Int32](cmsimplequeuegetcount(_:).md)
  Returns the number of elements currently in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeuegethead(_:))*