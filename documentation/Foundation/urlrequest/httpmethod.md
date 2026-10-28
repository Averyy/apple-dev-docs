# httpMethod

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The HTTP request method.

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
var httpMethod: String? { get set }
```

## Mentions

- [Uploading data to a website](../uploading-data-to-a-website.md)

## Discussion

The default HTTP method is “GET”.

## See Also

### Accessing request components
- [var url: URL?](./url.md)
  The URL of the request.
- [var httpBody: Data?](./httpbody.md)
  The data sent as the message body of a request, such as for an HTTP POST request.
- [var httpBodyStream: InputStream?](./httpbodystream.md)
  The stream used to deliver the HTTP body.
- [var mainDocumentURL: URL?](./maindocumenturl.md)
  The main document URL associated with this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/httpmethod)*