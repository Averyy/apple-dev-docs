# httpBodyStream

**Framework**: Foundation  
**Kind**: property

The request body as an input stream.

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
var httpBodyStream: InputStream? { get }
```

#### Discussion

`nil` if the body stream has not been set. The returned stream is for examination only—it is not safe to manipulate the stream in any way.

The receiver will have either an HTTP body or an HTTP body stream, only one may be set for a request. A HTTP body stream is preserved when copying an [`NSURLRequest`](nsurlrequest.md) object, but is lost when a request is archived using the [`NSCoding`](nscoding.md) protocol.

## See Also

- [var httpBodyStream: InputStream?](nsmutableurlrequest/httpbodystream.md)
  The request body as an input stream.
- [var httpBody: Data?](nsmutableurlrequest/httpbody.md)
  The request body.
- [var httpMethod: String?](nsurlrequest/httpmethod.md)
  The HTTP request method.
- [var url: URL?](nsurlrequest/url.md)
  The URL being requested.
- [var httpBody: Data?](nsurlrequest/httpbody.md)
  The request body.
- [var mainDocumentURL: URL?](nsurlrequest/maindocumenturl.md)
  The main document URL associated with the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/httpbodystream)*