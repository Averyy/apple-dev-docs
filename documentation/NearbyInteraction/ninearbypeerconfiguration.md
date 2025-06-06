# NINearbyPeerConfiguration

**Framework**: Nearby Interaction  
**Kind**: class

A configuration that enables interaction between iPhone or Apple Watch devices.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
class NINearbyPeerConfiguration
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Overview

A peer interaction session enables two Apple devices to share their respective distance and direction through the device’s Ultra Wideband (UWB) chip. To start a peer interaction session, create a [`NINearbyPeerConfiguration`](ninearbypeerconfiguration.md) instance and pass it to an [`NISession`](nisession.md) instance with the [`run(_:)`](nisession/run(_:).md) function.

For an example app that demonstrates this configuration, see [`Implementing Interactions Between Users in Close Proximity`](implementing-interactions-between-users-in-close-proximity.md).

##### Enable Precision Finding for Stationary Objects

In iOS 16, you can combine the visual spatial power of ARKit with the radio sensitivity of the UWB chip to locate stationary nearby objects with considerable precision. To do that, set [`isCameraAssistanceEnabled`](ninearbypeerconfiguration/iscameraassistanceenabled.md) to `true` and optionally provide the interaction session with an [`ARSession`](https://developer.apple.com/documentation/ARKit/ARSession) instance through [`setARSession(_:)`](nisession/setarsession(_:).md) before running the session. Together, the UWB chip and ARKit’s assistance enable Nearby Interaction to provide the same Precision Finding capabilities present in AirTag.

## Topics

### Creating a configuration
- [init(peerToken: NIDiscoveryToken)](ninearbypeerconfiguration/init(peertoken:).md)
  Creates a configuration for interaction between devices, including iPhone and Apple Watch.
### Accessing the discovery token
- [var peerDiscoveryToken: NIDiscoveryToken](ninearbypeerconfiguration/peerdiscoverytoken.md)
  A value that uniquely identifies the other peer in the interaction session.
### Subclassing a configuration
- [class NIConfiguration](niconfiguration.md)
  An abstract base class for interaction configurations.
### Enabling Camera Assistance
- [var isCameraAssistanceEnabled: Bool](ninearbypeerconfiguration/iscameraassistanceenabled.md)
  A Boolean value that combines the spatial awareness of ARKit with Nearby Interaction to improve the accuracy of a nearby object’s position.
### Checking distance measurement capability
- [var isExtendedDistanceMeasurementEnabled: Bool](ninearbypeerconfiguration/isextendeddistancemeasurementenabled.md)
  A Boolean value that indicates whether both peers can use extended distance measurement for this Nearby Interaction session instance.

## Relationships

### Inherits From
- [NIConfiguration](niconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Implementing Interactions Between Users in Close Proximity](implementing-interactions-between-users-in-close-proximity.md)
  Enable devices to access relative positioning information.
- [Discovering peers with Multipeer Connectivity](discovering-peers-with-multipeer-connectivity.md)
  Exchange discovery tokens over the local network.
- [Extending advanced direction finding and ranging](extending-advanced-direction-finding-and-ranging.md)
  Extend your app’s direction finding capabilities with data from Ultra Wideband devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbypeerconfiguration)*