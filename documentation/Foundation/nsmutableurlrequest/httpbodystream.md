# httpBodyStream

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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
var httpBodyStream: InputStream? { get set }
```

```objc
@property (retain, nullable) NSInputStream * HTTPBodyStream;
```

## Discussion

The request body of the receiver will be this input stream. The entire contents of the stream will be sent as the body, as in an HTTP `POST` request. The input stream should be unopened and the receiver will take over as the stream’s delegate.

Setting a body stream clears any data in [`httpBody`](./httpbody.md). These values are mutually exclusive.

## See Also

### Accessing request components
- [var httpMethod: String](./httpmethod.md)
  The HTTP request method.
- [var url: URL?](./url.md)
  The URL being requested.
- [var httpBody: Data?](./httpbody.md)
  The request body.
- [var mainDocumentURL: URL?](./maindocumenturl.md)
  The main document URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/httpbodystream)*