# URLSessionConfiguration.MultipathServiceType

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the type of service that Multipath TCP uses.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum MultipathServiceType
```

```c
enum NSURLSessionMultipathServiceType : NSInteger;
```

## Mentions

- [Improving network reliability using Multipath TCP](../improving-network-reliability-using-multipath-tcp.md)

## Topics

### Service types
- [URLSessionConfiguration.MultipathServiceType.none](./multipathservicetype-swift.enum/none.md)
  The default service type indicating that Multipath TCP should not be used.
- [URLSessionConfiguration.MultipathServiceType.handover](./multipathservicetype-swift.enum/handover.md)
  A Multipath TCP service that provides seamless handover between Wi-Fi and cellular in order to preserve the connection.
- [URLSessionConfiguration.MultipathServiceType.interactive](./multipathservicetype-swift.enum/interactive.md)
  A service whereby Multipath TCP attempts to use the lowest-latency interface.
- [URLSessionConfiguration.MultipathServiceType.aggregate](./multipathservicetype-swift.enum/aggregate.md)
  A service that aggregates the capacities of other Multipath options in an attempt to increase throughput and minimize latency.
### Initializers
- [init?(rawValue: Int)](./multipathservicetype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting Multipath TCP
- [Improving network reliability using Multipath TCP](../improving-network-reliability-using-multipath-tcp.md)
  Use the available radios in iOS devices to improve your app’s network reliability and performance.
- [var multipathServiceType: URLSessionConfiguration.MultipathServiceType](./multipathservicetype-swift.property.md)
  A service type that specifies the Multipath TCP connection policy for transmitting data over Wi-Fi and cellular interfaces.
- [Multipath Entitlement](../../BundleResources/entitlements/com.apple.developer.networking.multipath.md)
  A Boolean value indicating whether your app may use Multipath protocols to seamlessly transition between Wi-Fi and cellular networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum)*