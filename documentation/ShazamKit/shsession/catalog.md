# catalog

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly) SHCatalog * catalog;
```

*macOS*

```objc
@property (atomic, strong, readonly) SHCatalog * catalog;
```

## See Also

### Reading the session properties
- [var delegate: (any SHSessionDelegate)?](./delegate.md)
  The object that the session calls with the result of a match request.
- [var results: SHSession.Results](./results-swift.property.md)
  The results as an asynchronous sequence of matches.
- [SHSession.Results](./results-swift.struct.md)
  An asynchronous sequence that emits updates from a session object query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsession/catalog)*