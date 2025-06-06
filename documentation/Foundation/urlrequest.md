# URLRequest

**Framework**: Foundation  
**Kind**: struct

A URL load request that is independent of protocol or URL scheme.

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
struct URLRequest
```

## Mentions

- [Uploading data to a website](uploading-data-to-a-website.md)
- [Downloading files in the background](downloading-files-in-the-background.md)
- [Downloading files from websites](downloading-files-from-websites.md)
- [Uploading streams of data](uploading-streams-of-data.md)
- [Accessing cached data](accessing-cached-data.md)
- [Processing URL session data task results with Combine](processing-url-session-data-task-results-with-combine.md)

#### Overview

[`URLRequest`](urlrequest.md) encapsulates two essential properties of a load request: the URL to load and the policies used to load it. In addition, for HTTP and HTTPS requests, [`URLRequest`](urlrequest.md) includes the HTTP method (`GET`, `POST`, and so on) and the HTTP headers.

[`URLRequest`](urlrequest.md) only represents information about the request. Use other classes, such as [`URLSession`](urlsession.md), to send the request to a server. See [`Fetching website data into memory`](fetching-website-data-into-memory.md) and [`Uploading data to a website`](uploading-data-to-a-website.md) for an introduction to these techniques.

When writing Swift code, favor this structure over the [`NSURLRequest`](nsurlrequest.md) and [`NSMutableURLRequest`](nsmutableurlrequest.md) classes.

Certain header fields are reserved; see [`Reserved HTTP headers`](nsurlrequest#Reserved-HTTP-headers.md).

## Topics

### Creating a request
- [init(url: URL, cachePolicy: URLRequest.CachePolicy, timeoutInterval: TimeInterval)](urlrequest/init(url:cachepolicy:timeoutinterval:).md)
  Creates and initializes a URL request with the given URL, cache policy, and timeout interval.
### Working with a cache policy
- [var cachePolicy: URLRequest.CachePolicy](urlrequest/cachepolicy-swift.property.md)
  The request’s cache policy.
- [URLRequest.CachePolicy](urlrequest/cachepolicy-swift.typealias.md)
  An alias for the cache policy.
- [NSURLRequest.CachePolicy](nsurlrequest/cachepolicy-swift.enum.md)
  The constants used to specify interaction with the cached responses.
### Accessing request components
- [var httpMethod: String?](urlrequest/httpmethod.md)
  The HTTP request method.
- [var url: URL?](urlrequest/url.md)
  The URL of the request.
- [var httpBody: Data?](urlrequest/httpbody.md)
  The data sent as the message body of a request, such as for an HTTP POST request.
- [var httpBodyStream: InputStream?](urlrequest/httpbodystream.md)
  The stream used to deliver the HTTP body.
- [var mainDocumentURL: URL?](urlrequest/maindocumenturl.md)
  The main document URL associated with this request.
### Accessing header fields
- [var allHTTPHeaderFields: [String : String]?](urlrequest/allhttpheaderfields.md)
  A dictionary containing all of the HTTP header fields for a request.
- [func addValue(String, forHTTPHeaderField: String)](urlrequest/addvalue(_:forhttpheaderfield:).md)
  Adds a value to the header field.
- [func setValue(String?, forHTTPHeaderField: String)](urlrequest/setvalue(_:forhttpheaderfield:).md)
  Sets a value for the header field.
- [func value(forHTTPHeaderField: String) -> String?](urlrequest/value(forhttpheaderfield:).md)
  Retrieves a header value.
### Controlling request behavior
- [var timeoutInterval: TimeInterval](urlrequest/timeoutinterval.md)
  The timeout interval of the request.
- [var httpShouldHandleCookies: Bool](urlrequest/httpshouldhandlecookies.md)
  A Boolean value indicating whether cookies will be sent with and set for this request.
- [var httpShouldUsePipelining: Bool](urlrequest/httpshouldusepipelining.md)
  A Boolean value indicating whether the request should transmit before the previous response is received.
- [var allowsCellularAccess: Bool](urlrequest/allowscellularaccess.md)
  A Boolean value indicating whether the request is allowed to use the built-in cellular radios to satisfy the request.
- [var allowsPersistentDNS: Bool](urlrequest/allowspersistentdns.md)
- [var assumesHTTP3Capable: Bool](urlrequest/assumeshttp3capable.md)
- [var cookiePartitionIdentifier: String?](urlrequest/cookiepartitionidentifier.md)
- [var requiresDNSSECValidation: Bool](urlrequest/requiresdnssecvalidation.md)
### Supporting limited modes
- [var allowsConstrainedNetworkAccess: Bool](urlrequest/allowsconstrainednetworkaccess.md)
  A Boolean value that indicates whether the request may use the network when the user has specified Low Data Mode.
- [var allowsExpensiveNetworkAccess: Bool](urlrequest/allowsexpensivenetworkaccess.md)
  A Boolean value that indicates whether connections may use a network interface that the system considers expensive.
### Accessing the service type
- [var networkServiceType: URLRequest.NetworkServiceType](urlrequest/networkservicetype-swift.property.md)
  The type of network service for all tasks within network sessions to enable Cellular Network Slicing.
- [URLRequest.NetworkServiceType](urlrequest/networkservicetype-swift.typealias.md)
  An alias for the network service type.
- [NSURLRequest.NetworkServiceType](nsurlrequest/networkservicetype-swift.enum.md)
  Constants that specify how a request uses network resources.
### Indicating the source of the request
- [var attribution: URLRequest.Attribution](urlrequest/attribution-swift.property.md)
  The entity that initiates the network request.
- [URLRequest.Attribution](urlrequest/attribution-swift.typealias.md)
  A type that indicates the entities that can make a network request.
### Using reference types
- [class NSURLRequest](nsurlrequest.md)
  A URL load request that is independent of protocol or URL scheme.
- [class NSMutableURLRequest](nsmutableurlrequest.md)
  A mutable URL load request that is independent of protocol or URL scheme.
- [typealias MutableURLRequest](mutableurlrequest.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSURLRequest](nsurlrequest.md)
  A URL load request that is independent of protocol or URL scheme.
- [class NSMutableURLRequest](nsmutableurlrequest.md)
  A mutable URL load request that is independent of protocol or URL scheme.
- [class URLResponse](urlresponse.md)
  The metadata associated with the response to a URL load request, independent of protocol and URL scheme.
- [class HTTPURLResponse](httpurlresponse.md)
  The metadata associated with the response to an HTTP protocol URL load request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest)*