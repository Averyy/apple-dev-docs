# NSURLRequest

**Framework**: Foundation  
**Kind**: class

A URL load request that is independent of protocol or URL scheme.

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
class NSURLRequest
```

#### Overview

Use this type in Swift when you need reference semantics or other Foundation-specific behavior.

[`NSURLRequest`](nsurlrequest.md) encapsulates two essential properties of a load request: the URL to load and the policies used to load it. In addition, for HTTP and HTTPS requests, [`URLRequest`](urlrequest.md) includes the HTTP method (`GET`, `POST`, and so on) and the HTTP headers. Finally, custom protocols can support custom properties as explained in [`Custom protocol properties`](nsurlrequest#Custom-protocol-properties.md).

[`NSURLRequest`](nsurlrequest.md) only represents information about the request. Use other classes, such as [`URLSession`](urlsession.md), to send the request to a server. See [`Fetching website data into memory`](fetching-website-data-into-memory.md) and [`Uploading data to a website`](uploading-data-to-a-website.md) for an introduction to these techniques.

The mutable subclass of [`NSURLRequest`](nsurlrequest.md) is [`NSMutableURLRequest`](nsmutableurlrequest.md).

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`URLRequest`](urlrequest.md) structure, which bridges to the [`NSURLRequest`](nsurlrequest.md) class and its mutable subclass, [`NSMutableURLRequest`](nsmutableurlrequest.md). For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

##### Reserved Http Headers

The URL Loading System handles various aspects of the HTTP protocol for you (HTTP 1.1 persistent connections, proxies, authentication, and so on). As part of this support, the URL Loading System takes responsibility for certain HTTP headers:

- `Content-Length`
- `Authorization`
- `Connection`
- `Host`
- `Proxy-Authenticate`
- `Proxy-Authorization`
- `WWW-Authenticate`

If you set a value for one of these reserved headers, the system may ignore the value you set, or overwrite it with its own value, or simply not send it. Moreover, the exact behavior may change over time. To avoid confusing problems like this, do not set these headers directly.

The URL Loading System sets the `Content-Length` header based on whether the request body has a known length:

- If so, it uses the identity transfer encoding and sets the `Content-Length` header to that known length. You see this when you set the request body to a data object.
- If not, it uses the chunked transfer encoding and omits the `Content-Length` header. You see this when you set the request body to a stream.

##### Custom Protocol Properties

If you implement a custom URL protocol by subclassing [`URLProtocol`](urlprotocol.md), and it needs protocol-specific properties, extend [`NSURLRequest`](nsurlrequest.md) with accessor methods for those custom properties. In your accessor methods, call [`property(forKey:in:)`](urlprotocol/property(forkey:in:).md) and [`setProperty(_:forKey:in:)`](urlprotocol/setproperty(_:forkey:in:).md) to associate property values with the request.

## Topics

### Creating requests
- [convenience init(url: URL)](nsurlrequest/init(url:).md)
  Creates a URL request for a specified URL.
- [init(url: URL, cachePolicy: NSURLRequest.CachePolicy, timeoutInterval: TimeInterval)](nsurlrequest/init(url:cachepolicy:timeoutinterval:).md)
  Creates a URL request with the specified URL, cache policy, and timeout values.
### Working with a cache policy
- [var cachePolicy: NSURLRequest.CachePolicy](nsurlrequest/cachepolicy-swift.property.md)
  The request’s cache policy.
- [NSURLRequest.CachePolicy](nsurlrequest/cachepolicy-swift.enum.md)
  The constants used to specify interaction with the cached responses.
### Accessing request components
- [var httpMethod: String?](nsurlrequest/httpmethod.md)
  The HTTP request method.
- [var url: URL?](nsurlrequest/url.md)
  The URL being requested.
- [var httpBody: Data?](nsurlrequest/httpbody.md)
  The request body.
- [var httpBodyStream: InputStream?](nsurlrequest/httpbodystream.md)
  The request body as an input stream.
- [var mainDocumentURL: URL?](nsurlrequest/maindocumenturl.md)
  The main document URL associated with the request.
### Getting header fields
- [var allHTTPHeaderFields: [String : String]?](nsurlrequest/allhttpheaderfields.md)
  A dictionary containing all of the HTTP header fields for a request.
- [func value(forHTTPHeaderField: String) -> String?](nsurlrequest/value(forhttpheaderfield:).md)
  Returns the value of the specified HTTP header field.
### Controlling request behavior
- [var timeoutInterval: TimeInterval](nsurlrequest/timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldHandleCookies: Bool](nsurlrequest/httpshouldhandlecookies.md)
  A Boolean value that indicates whether the default cookie handling will be used for this request.
- [var httpShouldUsePipelining: Bool](nsurlrequest/httpshouldusepipelining.md)
  A Boolean value that indicates whether the request should continue transmitting data before receiving a response from an earlier transmission.
- [var allowsCellularAccess: Bool](nsurlrequest/allowscellularaccess.md)
  A Boolean value that indicates whether the request is allowed to use the cellular radio (if present).
### Supporting limited modes
- [var allowsConstrainedNetworkAccess: Bool](nsurlrequest/allowsconstrainednetworkaccess.md)
  A Boolean value that indicates whether connections may use the network when the user has specified Low Data Mode.
- [var allowsExpensiveNetworkAccess: Bool](nsurlrequest/allowsexpensivenetworkaccess.md)
  A Boolean value that indicates whether connections may use a network interface that the system considers expensive.
### Accessing the service type
- [var networkServiceType: NSURLRequest.NetworkServiceType](nsurlrequest/networkservicetype-swift.property.md)
  The network service type of the request.
- [NSURLRequest.NetworkServiceType](nsurlrequest/networkservicetype-swift.enum.md)
  Constants that specify how a request uses network resources.
### Supporting secure coding
- [class var supportsSecureCoding: Bool](nsurlrequest/supportssecurecoding.md)
  A Boolean value indicating whether the [`NSURLRequest`](nsurlrequest.md) implements the [`NSSecureCoding`](nssecurecoding.md) protocol.
### Indicating the source of the request
- [var attribution: NSURLRequest.Attribution](nsurlrequest/attribution-swift.property.md)
  The entity that initiates the network request.
- [NSURLRequest.Attribution](nsurlrequest/attribution-swift.enum.md)
  The entities that can make a network request.
### Instance Properties
- [var allowsPersistentDNS: Bool](nsurlrequest/allowspersistentdns.md)
- [var assumesHTTP3Capable: Bool](nsurlrequest/assumeshttp3capable.md)
- [var cookiePartitionIdentifier: String?](nsurlrequest/cookiepartitionidentifier.md)
- [var requiresDNSSECValidation: Bool](nsurlrequest/requiresdnssecvalidation.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSMutableURLRequest](nsmutableurlrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

- [struct URLRequest](urlrequest.md)
  A URL load request that is independent of protocol or URL scheme.
- [class NSMutableURLRequest](nsmutableurlrequest.md)
  A mutable URL load request that is independent of protocol or URL scheme.
- [class URLResponse](urlresponse.md)
  The metadata associated with the response to a URL load request, independent of protocol and URL scheme.
- [class HTTPURLResponse](httpurlresponse.md)
  The metadata associated with the response to an HTTP protocol URL load request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest)*