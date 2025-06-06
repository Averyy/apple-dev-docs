# mainDocumentURL

**Framework**: Foundation  
**Kind**: property

The main document URL.

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
var mainDocumentURL: URL? { get set }
```

#### Discussion

The caller should set the main document URL to an appropriate main document, if known. For example, when loading a web page the URL of the HTML document for the top-level frame would be appropriate. This URL will be used for the “only from same domain as main document” cookie accept policy.

`nil` indicates no main document.

## See Also

- [var httpMethod: String](nsmutableurlrequest/httpmethod.md)
  The HTTP request method.
- [var url: URL?](nsmutableurlrequest/url.md)
  The URL being requested.
- [var httpBody: Data?](nsmutableurlrequest/httpbody.md)
  The request body.
- [var httpBodyStream: InputStream?](nsmutableurlrequest/httpbodystream.md)
  The request body as an input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/maindocumenturl)*