# SHSession.Results

**Framework**: ShazamKit  
**Kind**: struct

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
- [func makeAsyncIterator() -> SHSession.Results.Iterator](shsession/results-swift.struct/makeasynciterator.md)
  Creates an asynchronous iterate that produces results from an asynchronous sequence.
- [SHSession.Results.Iterator](shsession/results-swift.struct/iterator.md)
  An interator for accessing session results.
- [SHSession.Results.Element](shsession/results-swift.struct/element.md)
  A set of results that a session result object returns.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var delegate: (any SHSessionDelegate)?](shsession/delegate.md)
  The object that the session calls with the result of a match request.
- [var catalog: SHCatalog](shsession/catalog.md)
  The catalog object containing the reference signatures and their associated metadata that the session uses to perform matches.
- [var results: SHSession.Results](shsession/results-swift.property.md)
  The results as an asynchronous sequence of matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsession/results-swift.struct)*