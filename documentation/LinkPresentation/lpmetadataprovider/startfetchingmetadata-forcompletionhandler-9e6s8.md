# startFetchingMetadata(for:completionHandler:)

**Framework**: Link Presentation  
**Kind**: method

Fetches metadata for the given `NSURLRequest`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func startFetchingMetadata(for request: URLRequest) async throws -> LPLinkMetadata
```

#### Discussion

Call this method once per [`LPMetadataProvider`](lpmetadataprovider.md) instance. If you attempt to fetch metadata multiple times on a single [`LPMetadataProvider`](lpmetadataprovider.md) instance, it throws an error.

The completion handler executes on a background queue. Dispatch any necessary UI updates back to the main queue. When the completion handler returns, it deletes any file URLs returned in the resulting [`LPLinkMetadata`](lplinkmetadata.md).

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
 func startFetchingMetadata(for request: URLRequest) async throws -> LPLinkMetadata
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
 func startFetchingMetadata(for request: URLRequest) async throws -> LPLinkMetadata
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lpmetadataprovider/startfetchingmetadata(for:completionhandler:)-9e6s8)*