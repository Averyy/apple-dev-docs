# URLSessionConfiguration.MultipathServiceType.aggregate

**Framework**: Foundation  
**Kind**: case

A service that aggregates the capacities of other Multipath options in an attempt to increase throughput and minimize latency.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case aggregate
```

#### Discussion

This option is available only for experimentation. Specify it for connections that use cellular data. You must also set the [`Multipath Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.multipath) in the Xcode Capabilities pane for your app.

To enable the aggregation mode, open the Settings app on your development iPhone and navigate to Developer, and then turn on Multipath Networking.

Multipath Aggregation requires an iOS device in Developer mode with a cellular connection running iOS 11.0 or later.

> **Note**:  Setting this option will use a considerable amount of cellular data.

## See Also

- [URLSessionConfiguration.MultipathServiceType.none](urlsessionconfiguration/multipathservicetype-swift.enum/none.md)
  The default service type indicating that Multipath TCP should not be used.
- [URLSessionConfiguration.MultipathServiceType.handover](urlsessionconfiguration/multipathservicetype-swift.enum/handover.md)
  A Multipath TCP service that provides seamless handover between Wi-Fi and cellular in order to preserve the connection.
- [URLSessionConfiguration.MultipathServiceType.interactive](urlsessionconfiguration/multipathservicetype-swift.enum/interactive.md)
  A service whereby Multipath TCP attempts to use the lowest-latency interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum/aggregate)*