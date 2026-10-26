---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbuffersequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncBufferSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that buffers elements in regard to a policy.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncBufferSequence<Base> where Base : Sendable, Base : AsyncSequence
```

## Topics

### Structures
- [AsyncBufferSequence.Iterator](./asyncbuffersequence/iterator.md)
### Instance Methods
- [func makeAsyncIterator() -> AsyncBufferSequence<Base>.Iterator](./asyncbuffersequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncBufferSequence.AsyncIterator](./asyncbuffersequence/asynciterator.md)
- [AsyncBufferSequence.Element](./asyncbuffersequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncbuffersequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncbuffersequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbuffersequence)*