# url

**Framework**: Link Presentation  
**Kind**: property

The URL that returned the metadata, taking server-side redirects into account.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var url: URL? { get set }
```

#### Discussion

The URL that returns the metadata may differ from the [`originalURL`](lplinkmetadata/originalurl.md) to which you sent the metadata request. This can happen if the server redirects the request, for example, when a resource has moved, or when the original URL is a domain alias.

## See Also

- [var originalURL: URL?](lplinkmetadata/originalurl.md)
  The original URL of the metadata request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lplinkmetadata/url)*