# cancel()

**Framework**: Link Presentation  
**Kind**: method

Cancels a metadata request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 18.0+
- visionOS 1.0+

## Declaration

```swift
func cancel()
```

#### Discussion

This method invokes the completion handler with the error code [`LPError.Code.metadataFetchCancelled`](lperror/code/metadatafetchcancelled.md) if the request hasn’t already completed.

## See Also

- [func startFetchingMetadata(for: URL, completionHandler: (LPLinkMetadata?, (any Error)?) -> Void)](lpmetadataprovider/startfetchingmetadata(for:completionhandler:)-54z5i.md)
  Fetches metadata for the given URL.
- [var shouldFetchSubresources: Bool](lpmetadataprovider/shouldfetchsubresources.md)
  A Boolean value indicating whether to download subresources specified by the metadata.
- [var timeout: TimeInterval](lpmetadataprovider/timeout.md)
  The time interval after which the request automatically fails if it hasn’t already completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lpmetadataprovider/cancel())*