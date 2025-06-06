# catalog

**Framework**: ShazamKit  
**Kind**: property

The catalog object containing the reference signatures and their associated metadata that the session uses to perform matches.

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
var catalog: SHCatalog { get }
```

## See Also

- [var delegate: (any SHSessionDelegate)?](shsession/delegate.md)
  The object that the session calls with the result of a match request.
- [var results: SHSession.Results](shsession/results-swift.property.md)
  The results as an asynchronous sequence of matches.
- [SHSession.Results](shsession/results-swift.struct.md)
  An asynchronous sequence that emits updates from a session object query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsession/catalog)*