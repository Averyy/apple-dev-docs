# startFetchingMetadata(for:completionHandler:)

**Framework**: Link Presentation  
**Kind**: method  
**Role**: Instance Method

Fetches metadata for the given URL.

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
func startFetchingMetadata(for URL: URL, completionHandler: @escaping @Sendable (LPLinkMetadata?, (any Error)?) -> Void)
```

```swift
func startFetchingMetadata(for URL: URL) async throws -> LPLinkMetadata
```

```objc
- (void) startFetchingMetadataForURL:(NSURL *) URL completionHandler:(void (^)(LPLinkMetadata *metadata, NSError *error)) completionHandler;
```

## Discussion

Call this method once per [`LPMetadataProvider`](../lpmetadataprovider.md) instance. If you attempt to fetch metadata multiple times on a single [`LPMetadataProvider`](../lpmetadataprovider.md) instance, it throws an error.

The completion handler executes on a background queue. Dispatch any necessary UI updates back to the main queue. When the completion handler returns, it deletes any file URLs returned in the resulting [`LPLinkMetadata`](../lplinkmetadata.md).

## See Also

### Fetching metadata
- [func cancel()](./cancel%28%29.md)
  Cancels a metadata request.
- [var shouldFetchSubresources: Bool](./shouldfetchsubresources.md)
  A Boolean value indicating whether to download subresources specified by the metadata.
- [var timeout: TimeInterval](./timeout.md)
  The time interval after which the request automatically fails if it hasn’t already completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lpmetadataprovider/startfetchingmetadata(for:completionhandler:)-54z5i)*