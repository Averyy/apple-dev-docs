# timeout

**Framework**: Link Presentation  
**Kind**: property  
**Role**: Instance Property

The time interval after which the request automatically fails if it hasn’t already completed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var timeout: TimeInterval { get set }
```

```objc
@property (nonatomic) NSTimeInterval timeout;
```

#### Discussion

The default timeout interval is 30 seconds. If a metadata fetch takes longer than the timeout interval, the completion handler is called with the error code [`LPError.Code.metadataFetchTimedOut`](../lperror/code/metadatafetchtimedout.md).

## See Also

### Fetching metadata
- [func startFetchingMetadata(for: URL, completionHandler: (LPLinkMetadata?, (any Error)?) -> Void)](./startfetchingmetadata%28for,completionhandler%29-54z5i.md)
  Fetches metadata for the given URL.
- [func cancel()](./cancel%28%29.md)
  Cancels a metadata request.
- [var shouldFetchSubresources: Bool](./shouldfetchsubresources.md)
  A Boolean value indicating whether to download subresources specified by the metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lpmetadataprovider/timeout)*