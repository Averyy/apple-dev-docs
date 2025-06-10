# httpAdditionalHeaders

**Framework**: Foundation  
**Kind**: property

A dictionary of additional headers to send with requests.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var httpAdditionalHeaders: [AnyHashable : Any]? { get set }
```

#### Discussion

This property specifies additional headers that are added to all tasks within sessions based on this configuration. For example, you might set the `User-Agent` header so that it is automatically included in every request your app makes through sessions based on this configuration.

An [`URLSession`](urlsession.md) object is designed to handle various aspects of the HTTP protocol for you. As a result, you should not modify the following headers:

- `Authorization`
- `Connection`
- `Host`
- `Proxy-Authenticate`
- `Proxy-Authorization`
- `WWW-Authenticate`

Additionally, if the length of your upload body data can be determined automatically—for example, if you provide the body content with an [`NSData`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) object—the value of `Content-Length` is set for you.

If the same header appears in both this array and the request object (where applicable), the request object’s value takes precedence.

The default value is an empty array.

## See Also

- [var identifier: String?](urlsessionconfiguration/identifier.md)
  The background session identifier of the configuration object.
- [var networkServiceType: NSURLRequest.NetworkServiceType](urlsessionconfiguration/networkservicetype.md)
  The type of network service for all tasks within network sessions to enable Cellular Network Slicing.
- [var allowsCellularAccess: Bool](urlsessionconfiguration/allowscellularaccess.md)
  A Boolean value that determines whether connections should be made over a cellular network.
- [var timeoutIntervalForRequest: TimeInterval](urlsessionconfiguration/timeoutintervalforrequest.md)
  The timeout interval to use when waiting for additional data.
- [var timeoutIntervalForResource: TimeInterval](urlsessionconfiguration/timeoutintervalforresource.md)
  The maximum amount of time that a resource request should be allowed to take.
- [var sharedContainerIdentifier: String?](urlsessionconfiguration/sharedcontaineridentifier.md)
  The identifier for the shared container into which files in background URL sessions should be downloaded.
- [var waitsForConnectivity: Bool](urlsessionconfiguration/waitsforconnectivity.md)
  A Boolean value that indicates whether the session should wait for connectivity to become available, or fail immediately.
- [var usesClassicLoadingMode: Bool](urlsessionconfiguration/usesclassicloadingmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/httpadditionalheaders)*