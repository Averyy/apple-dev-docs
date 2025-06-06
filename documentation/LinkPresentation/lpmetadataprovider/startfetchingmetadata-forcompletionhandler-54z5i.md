# startFetchingMetadata(for:completionHandler:)

**Framework**: Link Presentation  
**Kind**: method

Fetches metadata for the given URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 18.0+
- visionOS 1.0+

## Declaration

```swift
func startFetchingMetadata(for URL: URL) async throws -> LPLinkMetadata
```

#### Discussion

Call this method once per [`LPMetadataProvider`](lpmetadataprovider.md) instance. If you attempt to fetch metadata multiple times on a single [`LPMetadataProvider`](lpmetadataprovider.md) instance, it throws an error.

The completion handler executes on a background queue. Dispatch any necessary UI updates back to the main queue. When the completion handler returns, it deletes any file URLs returned in the resulting [`LPLinkMetadata`](lplinkmetadata.md).

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
 func startFetchingMetadata(for url: URL) async throws -> LPLinkMetadata
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
 func startFetchingMetadata(for url: URL) async throws -> LPLinkMetadata
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## See Also

- [func cancel()](lpmetadataprovider/cancel.md)
  Cancels a metadata request.
- [var shouldFetchSubresources: Bool](lpmetadataprovider/shouldfetchsubresources.md)
  A Boolean value indicating whether to download subresources specified by the metadata.
- [var timeout: TimeInterval](lpmetadataprovider/timeout.md)
  The time interval after which the request automatically fails if it hasn’t already completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lpmetadataprovider/startfetchingmetadata(for:completionhandler:)-54z5i)*