# enqueue(_:)

**Framework**: Core Media  
**Kind**: method

Enqueues an element in the queue.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func enqueue(_ element: UnsafeRawPointer) throws
```

## Parameters

- `element`: The element to enqueue.

## See Also

- [func dequeue() -> UnsafeRawPointer?](cmsimplequeue/dequeue.md)
  Dequeues an element from the queue.
- [func reset() throws](cmsimplequeue/reset.md)
  Resets the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeue/enqueue(_:))*