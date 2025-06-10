# HTTPURLResponse

**Framework**: Foundation  
**Kind**: class

The metadata associated with the response to an HTTP protocol URL load request.

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
class HTTPURLResponse
```

#### Overview

The [`HTTPURLResponse`](httpurlresponse.md) class is a subclass of [`URLResponse`](urlresponse.md) that provides methods for accessing information specific to HTTP protocol responses. Whenever you make HTTP URL load requests, any response objects you get back from the [`URLSession`](urlsession.md), [`NSURLConnection`](nsurlconnection.md), or [`NSURLDownload`](nsurldownload.md) class are instances of the [`HTTPURLResponse`](httpurlresponse.md) class.

## Topics

### Initializing a response object
- [init?(url: URL, statusCode: Int, httpVersion: String?, headerFields: [String : String]?)](httpurlresponse/init(url:statuscode:httpversion:headerfields:).md)
  Initializes an HTTP URL response object with a status code, protocol version, and response headers.
### Getting HTTP response headers
- [var allHeaderFields: [AnyHashable : Any]](httpurlresponse/allheaderfields.md)
  All HTTP header fields of the response.
- [func value(forHTTPHeaderField: String) -> String?](httpurlresponse/value(forhttpheaderfield:).md)
  Returns the value that corresponds to the given header field.
### Getting response status codes
- [class func localizedString(forStatusCode: Int) -> String](httpurlresponse/localizedstring(forstatuscode:).md)
  Returns a localized string corresponding to a specified HTTP status code.
- [var statusCode: Int](httpurlresponse/statuscode.md)
  The response’s HTTP status code.

## Relationships

### Inherits From
- [URLResponse](urlresponse.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct URLRequest](urlrequest.md)
  A URL load request that is independent of protocol or URL scheme.
- [class NSURLRequest](nsurlrequest.md)
  A URL load request that is independent of protocol or URL scheme.
- [class NSMutableURLRequest](nsmutableurlrequest.md)
  A mutable URL load request that is independent of protocol or URL scheme.
- [class URLResponse](urlresponse.md)
  The metadata associated with the response to a URL load request, independent of protocol and URL scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpurlresponse)*