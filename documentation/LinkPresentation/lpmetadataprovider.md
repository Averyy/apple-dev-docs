# LPMetadataProvider

**Framework**: Link Presentation  
**Kind**: class

An object that retrieves metadata for a URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 18.0+
- visionOS 1.0+

## Declaration

```swift
class LPMetadataProvider
```

#### Overview

Use [`LPMetadataProvider`](lpmetadataprovider.md) to fetch metadata for a URL, including its title, icon, and image or video links. All properties on the resulting [`LPLinkMetadata`](lplinkmetadata.md) instance are optional.

> **Note**: To enable macOS clients to fetch metadata for remote URLs, add the [`com.apple.security.network.client`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.network.client) entitlement.

To enable macOS clients to fetch metadata for remote URLs, add the [`com.apple.security.network.client`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.network.client) entitlement.

#### Fetch Link Metadata From a Url

For each metadata request, create an instance of [`LPMetadataProvider`](lpmetadataprovider.md) and call [`startFetchingMetadata(for:completionHandler:)`](lpmetadataprovider/startfetchingmetadata(for:completionhandler:)-54z5i.md).

In the completion handler, check the error. If your user doesn’t have a network connection, the fetch can fail. If the server doesn’t respond or is too slow, the fetch can time out. Alternatively, the app may cancel the request, or an unknown error may occur.

Otherwise, use the metadata however you want, for example, to populate the title for a table view cell.

```swift
let metadataProvider = LPMetadataProvider()
let url = URL(string: "https://www.apple.com/ipad")!

metadataProvider.startFetchingMetadata(for: url) { metadata, error in
    if error != nil {
        // The fetch failed; handle the error.
        return
    }

    // Make use of fetched metadata.
}
```

For more information about handling errors, see [`LPError`](lperror.md).

## Topics

### Fetching metadata
- [func startFetchingMetadata(for: URL, completionHandler: (LPLinkMetadata?, (any Error)?) -> Void)](lpmetadataprovider/startfetchingmetadata(for:completionhandler:)-54z5i.md)
  Fetches metadata for the given URL.
- [func cancel()](lpmetadataprovider/cancel.md)
  Cancels a metadata request.
- [var shouldFetchSubresources: Bool](lpmetadataprovider/shouldfetchsubresources.md)
  A Boolean value indicating whether to download subresources specified by the metadata.
- [var timeout: TimeInterval](lpmetadataprovider/timeout.md)
  The time interval after which the request automatically fails if it hasn’t already completed.
### Instance Methods
- [func startFetchingMetadata(for: URLRequest, completionHandler: (LPLinkMetadata?, (any Error)?) -> Void)](lpmetadataprovider/startfetchingmetadata(for:completionhandler:)-9e6s8.md)
  Fetches metadata for the given `NSURLRequest`.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class LPLinkMetadata](lplinkmetadata.md)
  An object that contains metadata about a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lpmetadataprovider)*