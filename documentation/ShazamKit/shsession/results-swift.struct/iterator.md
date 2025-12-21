# SHSession.Results.Iterator

**Framework**: ShazamKit  
**Kind**: struct

An iterator for accessing session results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Iterating over results
- [func next() async -> SHSession.Results.Element?](shsession/results-swift.struct/iterator/next.md)
  Asynchronously waits for the next element and returns it.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> SHSession.Results.Iterator](shsession/results-swift.struct/makeasynciterator.md)
  Creates an asynchronous iterate that produces results from an asynchronous sequence.
- [SHSession.Results.Element](shsession/results-swift.struct/element.md)
  A set of results that a session result object returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsession/results-swift.struct/iterator)*