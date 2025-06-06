# ObjectCaptureSession.Updates

**Framework**: RealityKit  
**Kind**: struct

Used to provide an `AsyncSequence` of change events for the observable properties.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
struct Updates<Element> where Element : Sendable
```

## Topics

### Structures
- [ObjectCaptureSession.Updates.Iterator](objectcapturesession/updates/iterator.md)
### Instance Methods
- [func makeAsyncIterator() -> ObjectCaptureSession.Updates<Element>.Iterator](objectcapturesession/updates/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
### Type Aliases
- [ObjectCaptureSession.Updates.AsyncIterator](objectcapturesession/updates/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](objectcapturesession/updates/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/updates)*