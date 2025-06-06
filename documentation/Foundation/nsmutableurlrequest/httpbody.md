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
var httpBody: Data? { get set }
```

#### Discussion

The request body is sent as the message body of the request, as in an HTTP `POST` request. Setting the HTTP body data clears any input stream in [`httpBodyStream`](nsmutableurlrequest/httpbodystream.md). These values are mutually exclusive.

## See Also

- [var httpMethod: String](nsmutableurlrequest/httpmethod.md)
  The HTTP request method.
- [var url: URL?](nsmutableurlrequest/url.md)
  The URL being requested.
- [var httpBodyStream: InputStream?](nsmutableurlrequest/httpbodystream.md)
  The request body as an input stream.
- [var mainDocumentURL: URL?](nsmutableurlrequest/maindocumenturl.md)
  The main document URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/httpbody)*