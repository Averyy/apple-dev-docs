# mainDocumentURL

**Framework**: Foundation  
**Kind**: property

The main document URL associated with the request.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var mainDocumentURL: URL? { get }
```

#### Discussion

This URL is used for the cookie “same domain as main document” policy.

## See Also

- [var mainDocumentURL: URL?](nsmutableurlrequest/maindocumenturl.md)
  The main document URL.
- [var httpMethod: String?](nsurlrequest/httpmethod.md)
  The HTTP request method.
- [var url: URL?](nsurlrequest/url.md)
  The URL being requested.
- [var httpBody: Data?](nsurlrequest/httpbody.md)
  The request body.
- [var httpBodyStream: InputStream?](nsurlrequest/httpbodystream.md)
  The request body as an input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/maindocumenturl)*