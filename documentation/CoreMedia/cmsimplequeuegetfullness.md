# CMSimpleQueueGetFullness

**Framework**: Core Media  
**Kind**: macro  
**Role**: Macro

A convenience macro that returns a queue’s fullness as a percentage of its capacity.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define CMSimpleQueueGetFullness(queue)
```

#### Return Value

- Returns `0.0` if the queue is empty.

#### Overview

- Returns `0.5` if the queue is half full.
- Returns `1.0` if the queue is full.
- Returns `0.0` if there is an error (for example, if the queue is `NULL`).

## See Also

### Inspecting Queues
- [func CMSimpleQueueGetHead(CMSimpleQueue) -> UnsafeRawPointer?](./cmsimplequeuegethead%28_%29.md)
  Returns the element at the head of the queue.
- [func CMSimpleQueueGetCapacity(CMSimpleQueue) -> Int32](./cmsimplequeuegetcapacity%28_%29.md)
  Returns the number of elements that the queue can hold.
- [func CMSimpleQueueGetCount(CMSimpleQueue) -> Int32](./cmsimplequeuegetcount%28_%29.md)
  Returns the number of elements currently in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeuegetfullness)*