# URLSessionConfiguration.MultipathServiceType.handover

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

A Multipath TCP service that provides seamless handover between Wi-Fi and cellular in order to preserve the connection.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case handover
```

```c
NSURLSessionMultipathServiceTypeHandover
```

## Discussion

Specify this option for long-lived or persistent connections. You must also set the [`Multipath Entitlement`](../../../BundleResources/entitlements/com.apple.developer.networking.multipath.md) in the Xcode Capabilities pane for your app.

## See Also

### Service types
- [URLSessionConfiguration.MultipathServiceType.none](./none.md)
  The default service type indicating that Multipath TCP should not be used.
- [URLSessionConfiguration.MultipathServiceType.interactive](./interactive.md)
  A service whereby Multipath TCP attempts to use the lowest-latency interface.
- [URLSessionConfiguration.MultipathServiceType.aggregate](./aggregate.md)
  A service that aggregates the capacities of other Multipath options in an attempt to increase throughput and minimize latency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum/handover)*