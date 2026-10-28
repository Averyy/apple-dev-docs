# shouldFetchSubresources

**Framework**: Link Presentation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to download subresources specified by the metadata.

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
var shouldFetchSubresources: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldFetchSubresources;
```

## Discussion

Subresources include the icon, image, or video. When set to `false`, the returned [`LPLinkMetadata`](../lplinkmetadata.md) object consists only of metadata retrieved from the main resource identified by the url passed to [`startFetchingMetadata(for:completionHandler:)`](./startfetchingmetadata%28for,completionhandler%29-54z5i.md).

The default value is `true`.

## See Also

### Fetching metadata
- [func startFetchingMetadata(for: URL, completionHandler: (LPLinkMetadata?, (any Error)?) -> Void)](./startfetchingmetadata%28for,completionhandler%29-54z5i.md)
  Fetches metadata for the given URL.
- [func cancel()](./cancel%28%29.md)
  Cancels a metadata request.
- [var timeout: TimeInterval](./timeout.md)
  The time interval after which the request automatically fails if it hasn’t already completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lpmetadataprovider/shouldfetchsubresources)*