# URLSessionConfiguration.MultipathServiceType.none

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

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

```c
NSURLSessionMultipathServiceTypeNone
```

## See Also

### Service types
- [URLSessionConfiguration.MultipathServiceType.handover](./handover.md)
  A Multipath TCP service that provides seamless handover between Wi-Fi and cellular in order to preserve the connection.
- [URLSessionConfiguration.MultipathServiceType.interactive](./interactive.md)
  A service whereby Multipath TCP attempts to use the lowest-latency interface.
- [URLSessionConfiguration.MultipathServiceType.aggregate](./aggregate.md)
  A service that aggregates the capacities of other Multipath options in an attempt to increase throughput and minimize latency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum/none)*