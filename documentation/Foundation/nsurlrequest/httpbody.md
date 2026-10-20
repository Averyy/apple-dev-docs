# httpBody

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly, nullable) NSData * HTTPBody;
```

#### Discussion

This data is sent as the message body of a request, as in an HTTP `POST` request.

## See Also

### Related Documentation
- [var httpBodyStream: InputStream?](../nsmutableurlrequest/httpbodystream.md)
  The request body as an input stream.
- [var httpBody: Data?](../nsmutableurlrequest/httpbody.md)
  The request body.
### Accessing request components
- [var httpMethod: String?](./httpmethod.md)
  The HTTP request method.
- [var url: URL?](./url.md)
  The URL being requested.
- [var httpBodyStream: InputStream?](./httpbodystream.md)
  The request body as an input stream.
- [var mainDocumentURL: URL?](./maindocumenturl.md)
  The main document URL associated with the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/httpbody)*