# CMSimpleQueueGetCapacity(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the number of elements that the queue can hold.

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
func CMSimpleQueueGetCapacity(_ queue: CMSimpleQueue) -> Int32
```

```c
extern int32_t CMSimpleQueueGetCapacity(CMSimpleQueueRef queue);
```

#### Return Value

The number of elements that the queue can hold. Returns `0` if there is an error.

## Parameters

- `queue`: The queue the function is interrogating. Must not be `NULL`.

## See Also

### Inspecting Queues
- [func CMSimpleQueueGetHead(CMSimpleQueue) -> UnsafeRawPointer?](./cmsimplequeuegethead%28_%29.md)
  Returns the element at the head of the queue.
- [func CMSimpleQueueGetCount(CMSimpleQueue) -> Int32](./cmsimplequeuegetcount%28_%29.md)
  Returns the number of elements currently in the queue.
- [CMSimpleQueueGetFullness](./cmsimplequeuegetfullness.md)
  A convenience macro that returns a queue’s fullness as a percentage of its capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeuegetcapacity(_:))*