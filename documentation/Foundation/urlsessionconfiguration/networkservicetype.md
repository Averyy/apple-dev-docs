# networkServiceType

**Framework**: Foundation  
**Kind**: property

The type of network service for all tasks within network sessions to enable Cellular Network Slicing.

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
var networkServiceType: NSURLRequest.NetworkServiceType { get set }
```

#### Discussion

To enable Cellular Network Slicing, you need to set the appropriate entitlements and properties.

Set the entitlements in your property list for [`5G Network Slicing App Category`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.slicing.appcategory) and [`5G Network Slicing Traffic Category`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.slicing.trafficcategory). If you don’t entitle your app by specifying both these entitlements, your apps network connections won’t be using Cellular Network Slicing, even if supported by the carrier.

At the time of network flow creation, set this to the appropriate [`NSURLRequest.NetworkServiceType`](nsurlrequest/networkservicetype-swift.enum.md) for your application type.

## See Also

- [var identifier: String?](urlsessionconfiguration/identifier.md)
  The background session identifier of the configuration object.
- [var httpAdditionalHeaders: [AnyHashable : Any]?](urlsessionconfiguration/httpadditionalheaders.md)
  A dictionary of additional headers to send with requests.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/networkservicetype)*