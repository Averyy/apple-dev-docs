# mainDocumentURL

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The main document URL associated with this request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var mainDocumentURL: URL? { get set }
```

#### Discussion

This URL is used for the cookie “same domain as main document” policy.

## See Also

### Accessing request components
- [var httpMethod: String?](./httpmethod.md)
  The HTTP request method.
- [var url: URL?](./url.md)
  The URL of the request.
- [var httpBody: Data?](./httpbody.md)
  The data sent as the message body of a request, such as for an HTTP POST request.
- [var httpBodyStream: InputStream?](./httpbodystream.md)
  The stream used to deliver the HTTP body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/maindocumenturl)*