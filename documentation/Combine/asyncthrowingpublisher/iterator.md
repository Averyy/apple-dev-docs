# AsyncThrowingPublisher.Iterator

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

The iterator that produces elements of the asynchronous publisher sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Iterating over elements
- [func next() async throws -> P.Output?](./iterator/next%28%29.md)
  Produces the next element in the prefix sequence.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../Swift/asynciteratorprotocol.md)

## See Also

### Creating an iterator
- [func makeAsyncIterator() -> AsyncThrowingPublisher<P>.Iterator](./makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/asyncthrowingpublisher/iterator)*