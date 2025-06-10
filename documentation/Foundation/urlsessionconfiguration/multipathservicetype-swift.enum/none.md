# URLSessionConfiguration.MultipathServiceType.none

**Framework**: Foundation  
**Kind**: case

The default service type indicating that Multipath TCP should not be used.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case none
```

## See Also

- [URLSessionConfiguration.MultipathServiceType.handover](urlsessionconfiguration/multipathservicetype-swift.enum/handover.md)
  A Multipath TCP service that provides seamless handover between Wi-Fi and cellular in order to preserve the connection.
- [URLSessionConfiguration.MultipathServiceType.interactive](urlsessionconfiguration/multipathservicetype-swift.enum/interactive.md)
  A service whereby Multipath TCP attempts to use the lowest-latency interface.
- [URLSessionConfiguration.MultipathServiceType.aggregate](urlsessionconfiguration/multipathservicetype-swift.enum/aggregate.md)
  A service that aggregates the capacities of other Multipath options in an attempt to increase throughput and minimize latency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum/none)*