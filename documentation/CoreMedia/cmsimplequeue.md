# CMSimpleQueue

**Framework**: Core Media  
**Kind**: class

A reference to an instance that provides a simple lockless queue of elements.

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
class CMSimpleQueue
```

## Topics

### Managing Queues
- [func enqueue(UnsafeRawPointer) throws](cmsimplequeue/enqueue(_:).md)
  Enqueues an element in the queue.
- [func dequeue() -> UnsafeRawPointer?](cmsimplequeue/dequeue.md)
  Dequeues an element from the queue.
- [func reset() throws](cmsimplequeue/reset.md)
  Resets the queue.
### Inspecting Queues
- [var head: UnsafeRawPointer?](cmsimplequeue/head.md)
  The head element in the queue.
- [var capacity: Int](cmsimplequeue/capacity.md)
  The number of elements that a queue can hold.
- [var count: Int](cmsimplequeue/count.md)
  The number of elements currently in the queue.
- [var fullness: Float](cmsimplequeue/fullness.md)
  The fullness of a queue as a percentage of its capacity.
### Accessing the Type Identifier
- [static var typeID: CFTypeID](cmsimplequeue/typeid.md)
  The type identifier of sample buffer objects.
### Errors
- [CMSimpleQueue.Error](cmsimplequeue/error.md)
  A structure that defines errors that queue operations can produce.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeue)*