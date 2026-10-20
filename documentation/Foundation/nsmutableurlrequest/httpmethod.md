# httpMethod

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The HTTP request method.

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
var httpMethod: String { get set }
```

```objc
@property (copy) NSString * HTTPMethod;
```

#### Discussion

The default HTTP method is “GET”.

## See Also

### Accessing request components
- [var url: URL?](./url.md)
  The URL being requested.
- [var httpBody: Data?](./httpbody.md)
  The request body.
- [var httpBodyStream: InputStream?](./httpbodystream.md)
  The request body as an input stream.
- [var mainDocumentURL: URL?](./maindocumenturl.md)
  The main document URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/httpmethod)*