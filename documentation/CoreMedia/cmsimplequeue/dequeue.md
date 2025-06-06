# dequeue()

**Framework**: Core Media  
**Kind**: method

Dequeues an element from the queue.

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
func dequeue() -> UnsafeRawPointer?
```

#### Return Value

A pointer to a dequeued element.

## See Also

- [func enqueue(UnsafeRawPointer) throws](cmsimplequeue/enqueue(_:).md)
  Enqueues an element in the queue.
- [func reset() throws](cmsimplequeue/reset.md)
  Resets the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeue/dequeue())*