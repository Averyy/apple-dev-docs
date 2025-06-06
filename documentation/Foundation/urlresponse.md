# URLResponse

**Framework**: Foundation  
**Kind**: class

The metadata associated with the response to a URL load request, independent of protocol and URL scheme.

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
class URLResponse
```

## Mentions

- [Processing URL session data task results with Combine](processing-url-session-data-task-results-with-combine.md)
- [Downloading files from websites](downloading-files-from-websites.md)

#### Overview

The related [`HTTPURLResponse`](httpurlresponse.md) class is a commonly used subclass of [`URLResponse`](urlresponse.md) whose objects represent a response to an HTTP URL load request and store additional protocol-specific information such as the response headers. Whenever you make an HTTP request, the [`URLResponse`](urlresponse.md) object you get back is actually an instance of the [`HTTPURLResponse`](httpurlresponse.md) class.

> **Note**:  [`URLResponse`](urlresponse.md) objects don’t contain the actual bytes representing the content of a URL. Instead, the data is returned either a piece at a time through delegate calls or in its entirety when the request completes, depending on the method and class used to initiate the request. Read [`Fetching website data into memory`](fetching-website-data-into-memory.md) to learn various ways to receive the content data from a URL load.

## Topics

### Creating a response
- [init(url: URL, mimeType: String?, expectedContentLength: Int, textEncodingName: String?)](urlresponse/init(url:mimetype:expectedcontentlength:textencodingname:).md)
  Creates an initialized [`URLResponse`](urlresponse.md) object with the URL, MIME type, length, and text encoding set to given values.
### Getting the response properties
- [var expectedContentLength: Int64](urlresponse/expectedcontentlength.md)
  The expected length of the response’s content.
- [var suggestedFilename: String?](urlresponse/suggestedfilename.md)
  A suggested filename for the response data.
- [var mimeType: String?](urlresponse/mimetype.md)
  The MIME type of the response.
- [var textEncodingName: String?](urlresponse/textencodingname.md)
  The name of the text encoding provided by the response’s originating source.
- [var url: URL?](urlresponse/url.md)
  The URL for the response.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [HTTPURLResponse](httpurlresponse.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct URLRequest](urlrequest.md)
  A URL load request that is independent of protocol or URL scheme.
- [class NSURLRequest](nsurlrequest.md)
  A URL load request that is independent of protocol or URL scheme.
- [class NSMutableURLRequest](nsmutableurlrequest.md)
  A mutable URL load request that is independent of protocol or URL scheme.
- [class HTTPURLResponse](httpurlresponse.md)
  The metadata associated with the response to an HTTP protocol URL load request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresponse)*