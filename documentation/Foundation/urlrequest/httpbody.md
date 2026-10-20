# httpBody

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The data sent as the message body of a request, such as for an HTTP POST request.

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
var httpBody: Data? { get set }
```

## See Also

### Accessing request components
- [var httpMethod: String?](./httpmethod.md)
  The HTTP request method.
- [var url: URL?](./url.md)
  The URL of the request.
- [var httpBodyStream: InputStream?](./httpbodystream.md)
  The stream used to deliver the HTTP body.
- [var mainDocumentURL: URL?](./maindocumenturl.md)
  The main document URL associated with this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/httpbody)*