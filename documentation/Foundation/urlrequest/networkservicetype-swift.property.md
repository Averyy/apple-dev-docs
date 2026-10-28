# networkServiceType

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The type of network service for all tasks within network sessions to enable Cellular Network Slicing.

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
var networkServiceType: URLRequest.NetworkServiceType { get set }
```

## Discussion

There are two steps to enable Cellular Network Slicing:

- Set the entitlements in your property list for [`5G Network Slicing App Category`](../../BundleResources/entitlements/com.apple.developer.networking.slicing.appcategory.md) and [`5G Network Slicing Traffic Category`](../../BundleResources/entitlements/com.apple.developer.networking.slicing.trafficcategory.md). If you don’t entitle your app by specifying both these entitlements, your apps network connections won’t be using Cellular Network Slicing, even if supported by the carrier.
- At the time of network flow creation, set this to the appropriate [`NSURLRequest.NetworkServiceType`](../nsurlrequest/networkservicetype-swift.enum.md) for your application type.

## See Also

### Accessing the service type
- [URLRequest.NetworkServiceType](./networkservicetype-swift.typealias.md)
  An alias for the network service type.
- [NSURLRequest.NetworkServiceType](../nsurlrequest/networkservicetype-swift.enum.md)
  Constants that specify how a request uses network resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/networkservicetype-swift.property)*