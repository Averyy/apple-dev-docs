# CMSimpleQueueGetCount(_:)

**Framework**: Core Media  
**Kind**: func

Returns the number of elements currently in the queue.

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
func CMSimpleQueueGetCount(_ queue: CMSimpleQueue) -> Int32
```

#### Return Value

The number of elements currently in the queue. Returns `0` if there is an error.

## Parameters

- `queue`: The queue the function is interrogating. Must not be  .

## See Also

- [func CMSimpleQueueGetHead(CMSimpleQueue) -> UnsafeRawPointer?](cmsimplequeuegethead(_:).md)
  Returns the element at the head of the queue.
- [func CMSimpleQueueGetCapacity(CMSimpleQueue) -> Int32](cmsimplequeuegetcapacity(_:).md)
  Returns the number of elements that the queue can hold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeuegetcount(_:))*