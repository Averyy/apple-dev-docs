# URLSessionConfiguration.MultipathServiceType.handover

**Framework**: Foundation  
**Kind**: case

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

#### Discussion

Specify this option for long-lived or persistent connections. You must also set the [`Multipath Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.multipath) in the Xcode Capabilities pane for your app.

## See Also

- [URLSessionConfiguration.MultipathServiceType.none](urlsessionconfiguration/multipathservicetype-swift.enum/none.md)
  The default service type indicating that Multipath TCP should not be used.
- [URLSessionConfiguration.MultipathServiceType.interactive](urlsessionconfiguration/multipathservicetype-swift.enum/interactive.md)
  A service whereby Multipath TCP attempts to use the lowest-latency interface.
- [URLSessionConfiguration.MultipathServiceType.aggregate](urlsessionconfiguration/multipathservicetype-swift.enum/aggregate.md)
  A service that aggregates the capacities of other Multipath options in an attempt to increase throughput and minimize latency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum/handover)*