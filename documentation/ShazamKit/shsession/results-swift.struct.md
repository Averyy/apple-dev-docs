# SHSession.Results

**Framework**: ShazamKit  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that emits updates from a session object query.

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
struct Results
```

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> SHSession.Results.Iterator](./results-swift.struct/makeasynciterator%28%29.md)
  Creates an asynchronous iterator that produces results from an asynchronous sequence.
- [SHSession.Results.Iterator](./results-swift.struct/iterator.md)
  An iterator for accessing session results.
- [SHSession.Results.Element](./results-swift.struct/element.md)
  A set of results that a session result object returns.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Reading the session properties
- [var delegate: (any SHSessionDelegate)?](./delegate.md)
  The object that the session calls with the result of a match request.
- [var catalog: SHCatalog](./catalog.md)
  The catalog object containing the reference signatures and their associated metadata that the session uses to perform matches.
- [var results: SHSession.Results](./results-swift.property.md)
  The results as an asynchronous sequence of matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsession/results-swift.struct)*