# SHSession.Results.Iterator

**Framework**: ShazamKit  
**Kind**: struct  
**Role**: Structure

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
- [func next() async -> SHSession.Results.Element?](./iterator/next%28%29.md)
  Asynchronously waits for the next element and returns it.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)

## See Also

### Creating an iterator
- [func makeAsyncIterator() -> SHSession.Results.Iterator](./makeasynciterator%28%29.md)
  Creates an asynchronous iterator that produces results from an asynchronous sequence.
- [SHSession.Results.Element](./element.md)
  A set of results that a session result object returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsession/results-swift.struct/iterator)*