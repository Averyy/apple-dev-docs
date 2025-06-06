# makeAsyncIterator()

**Framework**: Combine  
**Kind**: method

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

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
func makeAsyncIterator() -> AsyncPublisher<P>.Iterator
```

#### Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.

## See Also

- [AsyncPublisher.Iterator](asyncpublisher/iterator.md)
  The iterator that produces elements of the asynchronous publisher sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/asyncpublisher/makeasynciterator())*