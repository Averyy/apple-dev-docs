# url

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The URL being requested.

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
var url: URL? { get }
```

```objc
@property (copy, readonly, nullable) NSURL * URL;
```

## See Also

### Related Documentation
- [var url: URL?](../nsmutableurlrequest/url.md)
  The URL being requested.
### Accessing request components
- [var httpMethod: String?](./httpmethod.md)
  The HTTP request method.
- [var httpBody: Data?](./httpbody.md)
  The request body.
- [var httpBodyStream: InputStream?](./httpbodystream.md)
  The request body as an input stream.
- [var mainDocumentURL: URL?](./maindocumenturl.md)
  The main document URL associated with the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/url)*