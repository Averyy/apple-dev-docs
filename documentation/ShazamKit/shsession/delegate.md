# delegate

**Framework**: ShazamKit  
**Kind**: property

The object that the session calls with the result of a match request.

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
weak var delegate: (any SHSessionDelegate)? { get set }
```

## See Also

- [var catalog: SHCatalog](shsession/catalog.md)
  The catalog object containing the reference signatures and their associated metadata that the session uses to perform matches.
- [var results: SHSession.Results](shsession/results-swift.property.md)
  The results as an asynchronous sequence of matches.
- [SHSession.Results](shsession/results-swift.struct.md)
  An asynchronous sequence that emits updates from a session object query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsession/delegate)*