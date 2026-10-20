# NINearbyPeerConfiguration

**Framework**: Nearby Interaction  
**Kind**: class  
**Role**: Class

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

```objc
@interface NINearbyPeerConfiguration : NIConfiguration
```

## Mentions

- [Initiating and maintaining a session](./initiating-and-maintaining-a-session.md)

#### Overview

A peer interaction session enables two Apple devices to share their respective distance and direction through the device’s Ultra Wideband (UWB) chip. To start a peer interaction session, create a [`NINearbyPeerConfiguration`](./ninearbypeerconfiguration.md) instance and pass it to an [`NISession`](./nisession.md) instance with the [`run(_:)`](./nisession/run%28_%29.md) function.

For an example app that demonstrates this configuration, see [Implementing interactions between users in close proximity](./implementing-interactions-between-users-in-close-proximity.md).

##### Enable Precision Finding for stationary objects

In iOS 16, you can combine the visual spatial power of ARKit with the radio sensitivity of the UWB chip to locate stationary nearby objects with considerable precision. To do that, set [`isCameraAssistanceEnabled`](./ninearbypeerconfiguration/iscameraassistanceenabled.md) to `true` and optionally provide the interaction session with an [`ARSession`](../ARKit/arsession.md) instance through [`setARSession(_:)`](./nisession/setarsession%28_%29.md) before running the session. Together, the UWB chip and ARKit’s assistance enable Nearby Interaction to provide the same Precision Finding capabilities present in AirTag.

## Topics

### Creating a configuration
- [init(peerToken: NIDiscoveryToken)](./ninearbypeerconfiguration/init%28peertoken%29.md)
  Creates a configuration for interaction between devices, including iPhone and Apple Watch.
### Accessing the discovery token
- [var peerDiscoveryToken: NIDiscoveryToken](./ninearbypeerconfiguration/peerdiscoverytoken.md)
  A value that uniquely identifies the other peer in the interaction session.
### Subclassing a configuration
- [class NIConfiguration](./niconfiguration.md)
  An abstract base class for interaction configurations.
### Enabling Camera Assistance
- [var isCameraAssistanceEnabled: Bool](./ninearbypeerconfiguration/iscameraassistanceenabled.md)
  A Boolean value that combines the spatial awareness of ARKit with Nearby Interaction to improve the accuracy of a nearby object’s position.
### Checking distance measurement capability
- [var isExtendedDistanceMeasurementEnabled: Bool](./ninearbypeerconfiguration/isextendeddistancemeasurementenabled.md)
  A Boolean value that indicates whether both peers can use extended distance measurement for this Nearby Interaction session instance.

## Relationships

### Inherits From
- [NIConfiguration](./niconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbypeerconfiguration)*