# NSMutableURLRequest

**Framework**: Foundation  
**Kind**: class

A mutable URL load request that is independent of protocol or URL scheme.

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
class NSMutableURLRequest
```

#### Overview

In Swift, this object bridges to [`NSURLRequest`](nsurlrequest.md) and you use when you need reference semantics or other Foundation-specific behavior.

[`NSMutableURLRequest`](nsmutableurlrequest.md) is a subclass of [`NSURLRequest`](nsurlrequest.md) that allows you to change the request’s properties.

[`NSMutableURLRequest`](nsmutableurlrequest.md) only represents information about the request. Use other classes, such as [`URLSession`](urlsession.md), to send the request to a server. See [`Fetching website data into memory`](fetching-website-data-into-memory.md) and [`Uploading data to a website`](uploading-data-to-a-website.md) for an introduction to these techniques.

Classes that create a network operation based on a request make a deep copy of that request. Thus, changing the request after creating a network operation has no effect on the ongoing operation. For example, if you use [`dataTask(with:completionHandler:)`](urlsession/datatask(with:completionhandler:)-e6xv.md) to create a data task from a request, and then later change the request, the data task continues using the original request.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`URLRequest`](urlrequest.md) structure, which bridges to the [`NSMutableURLRequest`](nsmutableurlrequest.md) class and its immutable superclass, [`NSURLRequest`](nsurlrequest.md). For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Working with a cache policy
- [var cachePolicy: NSURLRequest.CachePolicy](nsmutableurlrequest/cachepolicy.md)
  The request’s cache policy.
- [NSURLRequest.CachePolicy](nsurlrequest/cachepolicy-swift.enum.md)
  The constants used to specify interaction with the cached responses.
### Accessing request components
- [var httpMethod: String](nsmutableurlrequest/httpmethod.md)
  The HTTP request method.
- [var url: URL?](nsmutableurlrequest/url.md)
  The URL being requested.
- [var httpBody: Data?](nsmutableurlrequest/httpbody.md)
  The request body.
- [var httpBodyStream: InputStream?](nsmutableurlrequest/httpbodystream.md)
  The request body as an input stream.
- [var mainDocumentURL: URL?](nsmutableurlrequest/maindocumenturl.md)
  The main document URL.
### Accessing header fields
- [var allHTTPHeaderFields: [String : String]?](nsmutableurlrequest/allhttpheaderfields.md)
  A dictionary containing all of the HTTP header fields for a request.
- [func addValue(String, forHTTPHeaderField: String)](nsmutableurlrequest/addvalue(_:forhttpheaderfield:).md)
  Adds a value to the header field.
- [func setValue(String?, forHTTPHeaderField: String)](nsmutableurlrequest/setvalue(_:forhttpheaderfield:).md)
  Sets a value for the header field.
### Controlling request behavior
- [var timeoutInterval: TimeInterval](nsmutableurlrequest/timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldHandleCookies: Bool](nsmutableurlrequest/httpshouldhandlecookies.md)
  A Boolean value that indicates whether the request should use the default cookie handling for the request.
- [var httpShouldUsePipelining: Bool](nsmutableurlrequest/httpshouldusepipelining.md)
  A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission.
- [var allowsCellularAccess: Bool](nsmutableurlrequest/allowscellularaccess.md)
  A Boolean value that indicates whether a connection can use the device’s cellular network (if present).
### Supporting limited modes
- [var allowsConstrainedNetworkAccess: Bool](nsmutableurlrequest/allowsconstrainednetworkaccess.md)
  A Boolean value that indicates whether connections may use the network when the user has specified Low Data Mode.
- [var allowsExpensiveNetworkAccess: Bool](nsmutableurlrequest/allowsexpensivenetworkaccess.md)
  A Boolean value that indicates whether connections may use a network interface that the system considers expensive.
### Accessing the service type
- [var networkServiceType: NSURLRequest.NetworkServiceType](nsmutableurlrequest/networkservicetype.md)
  The network service type of the connection.
- [NSURLRequest.NetworkServiceType](nsurlrequest/networkservicetype-swift.enum.md)
  Constants that specify how a request uses network resources.
### Working with hotspots
- [func bind(to: NEHotspotHelperCommand)](nsmutableurlrequest/bind(to:).md)
  Binds a URL request to the network interface associated with the hotspot helper command instance.
### Indicating the source of the request
- [var attribution: NSURLRequest.Attribution](nsmutableurlrequest/attribution.md)
  The entity that initiates the network request.
- [NSURLRequest.Attribution](nsurlrequest/attribution-swift.enum.md)
  The entities that can make a network request.
### Instance Properties
- [var allowsPersistentDNS: Bool](nsmutableurlrequest/allowspersistentdns.md)
- [var allowsUltraConstrainedNetworkAccess: Bool](nsmutableurlrequest/allowsultraconstrainednetworkaccess.md)
- [var assumesHTTP3Capable: Bool](nsmutableurlrequest/assumeshttp3capable.md)
- [var cookiePartitionIdentifier: String?](nsmutableurlrequest/cookiepartitionidentifier.md)
- [var requiresDNSSECValidation: Bool](nsmutableurlrequest/requiresdnssecvalidation.md)

## Relationships

### Inherits From
- [NSURLRequest](nsurlrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct URLRequest](urlrequest.md)
  A URL load request that is independent of protocol or URL scheme.
- [class NSURLRequest](nsurlrequest.md)
  A URL load request that is independent of protocol or URL scheme.
- [class URLResponse](urlresponse.md)
  The metadata associated with the response to a URL load request, independent of protocol and URL scheme.
- [class HTTPURLResponse](httpurlresponse.md)
  The metadata associated with the response to an HTTP protocol URL load request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest)*