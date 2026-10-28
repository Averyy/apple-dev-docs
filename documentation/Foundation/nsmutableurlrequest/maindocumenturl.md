# mainDocumentURL

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, nullable) NSURL * mainDocumentURL;
```

## Discussion

The caller should set the main document URL to an appropriate main document, if known. For example, when loading a web page the URL of the HTML document for the top-level frame would be appropriate. This URL will be used for the “only from same domain as main document” cookie accept policy.

`nil` indicates no main document.

## See Also

### Accessing request components
- [var httpMethod: String](./httpmethod.md)
  The HTTP request method.
- [var url: URL?](./url.md)
  The URL being requested.
- [var httpBody: Data?](./httpbody.md)
  The request body.
- [var httpBodyStream: InputStream?](./httpbodystream.md)
  The request body as an input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/maindocumenturl)*