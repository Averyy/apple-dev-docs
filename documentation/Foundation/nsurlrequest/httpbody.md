# httpBody

**Framework**: Foundation  
**Kind**: property

The request body.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var httpBody: Data? { get }
```

#### Discussion

This data is sent as the message body of a request, as in an HTTP `POST` request.

## See Also

- [var httpBodyStream: InputStream?](nsmutableurlrequest/httpbodystream.md)
  The request body as an input stream.
- [var httpBody: Data?](nsmutableurlrequest/httpbody.md)
  The request body.
- [var httpMethod: String?](nsurlrequest/httpmethod.md)
  The HTTP request method.
- [var url: URL?](nsurlrequest/url.md)
  The URL being requested.
- [var httpBodyStream: InputStream?](nsurlrequest/httpbodystream.md)
  The request body as an input stream.
- [var mainDocumentURL: URL?](nsurlrequest/maindocumenturl.md)
  The main document URL associated with the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/httpbody)*