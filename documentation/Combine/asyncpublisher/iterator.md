# AsyncPublisher.Iterator

**Framework**: Combine  
**Kind**: struct

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

### Iterating over Elements
- [func next() async -> P.Output?](asyncpublisher/iterator/next.md)
  Produces the next element in the prefix sequence.
### Type Aliases
- [AsyncPublisher.Iterator.Element](asyncpublisher/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](asyncpublisher/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> AsyncPublisher<P>.Iterator](asyncpublisher/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/asyncpublisher/iterator)*