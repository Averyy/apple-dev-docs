# multipathServiceType

**Framework**: Foundation  
**Kind**: property

A service type that specifies the Multipath TCP connection policy for transmitting data over Wi-Fi and cellular interfaces.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var multipathServiceType: URLSessionConfiguration.MultipathServiceType { get set }
```

## Mentions

- [Improving network reliability using Multipath TCP](improving-network-reliability-using-multipath-tcp.md)

#### Discussion

Multipath TCP, defined by the IETF in [`RFC 6824`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6824), is an extension to TCP that permits multiple interfaces to transmit a single data stream. This capability allows a seamless handover from Wi-Fi to cellular, aimed at making both interfaces more efficient and improving the user experience.

The [`multipathServiceType`](urlsessionconfiguration/multipathservicetype-swift.property.md) property defines which policy the Multipath TCP stack uses to schedule traffic across Wi-Fi and cellular interfaces. The default value is `none`, meaning Multipath TCP is disabled. You can also select handover mode, which provides seamless handover between Wi-Fi and cellular.

Multipath TCP requires server support. Resources for Linux-based systems are available at [`https://mptcp.dev`](https://developer.apple.comhttps://mptcp.dev).

## See Also

- [Improving network reliability using Multipath TCP](improving-network-reliability-using-multipath-tcp.md)
  Use the available radios in iOS devices to improve your app’s network reliability and performance.
- [URLSessionConfiguration.MultipathServiceType](urlsessionconfiguration/multipathservicetype-swift.enum.md)
  Constants that specify the type of service that Multipath TCP uses.
- [Multipath Entitlement](../BundleResources/Entitlements/com.apple.developer.networking.multipath.md)
  A Boolean value indicating whether your app may use Multipath protocols to seamlessly transition between Wi-Fi and cellular networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.property)*