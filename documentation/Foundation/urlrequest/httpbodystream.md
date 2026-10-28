# httpBodyStream

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The stream used to deliver the HTTP body.

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
var httpBodyStream: InputStream? { get set }
```

## Discussion

The stream is returned for examination only; it’s unsafe for the caller to manipulate the stream in any way.

> **Note**:  The [`httpBodyStream`](./httpbodystream.md) and [`httpBody`](./httpbody.md) are mutually exclusive - only one can be set on a given request. The body stream is preserved across copies, but is lost when the request is coded via the [`NSCoding`](../nscoding.md) protocol

## See Also

### Accessing request components
- [var httpMethod: String?](./httpmethod.md)
  The HTTP request method.
- [var url: URL?](./url.md)
  The URL of the request.
- [var httpBody: Data?](./httpbody.md)
  The data sent as the message body of a request, such as for an HTTP POST request.
- [var mainDocumentURL: URL?](./maindocumenturl.md)
  The main document URL associated with this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/httpbodystream)*