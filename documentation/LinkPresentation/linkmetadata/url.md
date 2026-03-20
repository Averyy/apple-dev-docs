# url

**Framework**: Link Presentation  
**Kind**: property

The URL that returned the metadata, taking server-side redirects into account.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
nonisolated
var url: URL { get set }
```

#### Discussion

The URL that returns the metadata may differ from the [`originalURL`](linkmetadata/originalurl.md) to which you sent the metadata request. This can happen if the server redirects the request, for example, when a resource has moved, or when the original URL is a domain alias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/linkmetadata/url)*