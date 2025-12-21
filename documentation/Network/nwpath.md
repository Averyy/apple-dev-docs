# NWPath

**Framework**: Network  
**Kind**: struct

An object that contains information about the properties of the network that a connection uses, or that are available to your app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
struct NWPath
```

## Topics

### Checking Path Availability
- [let status: NWPath.Status](nwpath/status-swift.property.md)
  A status indicating whether a path can be used by connections.
- [NWPath.Status](nwpath/status-swift.enum.md)
  Status values indicating whether a path can be used by connections.
### Inspecting Interfaces
- [func usesInterfaceType(NWInterface.InterfaceType) -> Bool](nwpath/usesinterfacetype(_:).md)
  Checks if connections using the path may send traffic over a specific interface type.
- [let availableInterfaces: [NWInterface]](nwpath/availableinterfaces.md)
  A list of all interfaces available to the path, in order of preference.
- [var gateways: [NWEndpoint]](nwpath/gateways.md)
  A list of gateways configured on the interfaces available to a path.
### Checking Path Capabilities
- [let supportsIPv4: Bool](nwpath/supportsipv4.md)
  A Boolean indicating whether the path can route IPv4 traffic.
- [let supportsIPv6: Bool](nwpath/supportsipv6.md)
  A Boolean indicating whether the path can route IPv6 traffic.
- [let supportsDNS: Bool](nwpath/supportsdns.md)
  A Boolean indicating whether the path has a DNS server configured.
- [var isConstrained: Bool](nwpath/isconstrained.md)
  A Boolean indicating whether the path uses an interface in Low Data Mode.
- [let isExpensive: Bool](nwpath/isexpensive.md)
  A Boolean indicating whether the path uses an interface that is considered expensive, such as Cellular or a Personal Hotspot.
### Inspecting Connected Paths
- [let localEndpoint: NWEndpoint?](nwpath/localendpoint.md)
  The local endpoint in use by a connection’s network path.
- [let remoteEndpoint: NWEndpoint?](nwpath/remoteendpoint.md)
  The remote endpoint in use by a connection’s network path.
### Instance Properties
- [var isUltraConstrained: Bool](nwpath/isultraconstrained.md)
  Checks if the path uses an NWInterface that is considered to be constrained by user preference
- [var linkQuality: NWPath.LinkQuality](nwpath/linkquality-swift.property.md)
  Represents the link quality measurement of the link layer network attachment
- [var unsatisfiedReason: NWPath.UnsatisfiedReason](nwpath/unsatisfiedreason-swift.property.md)
- [var wifiAware: WAPath?](nwpath/wifiaware.md)
  Current status and performance information for Wi-Fi Aware, or `nil` if this path is not over Wi-Fi Aware.
### Enumerations
- [NWPath.LinkQuality](nwpath/linkquality-swift.enum.md)
  Represents the link quality measurement of the link layer network attachment
- [NWPath.UnsatisfiedReason](nwpath/unsatisfiedreason-swift.enum.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NWPathMonitor](nwpathmonitor.md)
  An observer that you use to monitor and react to network changes.
- [struct NWInterface](nwinterface.md)
  An interface that a network connection uses to send and receive data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpath)*