# NINearbyAccessoryConfiguration

**Framework**: Nearby Interaction  
**Kind**: class

A configuration that enables interaction between iPhone and third-party accessories.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- watchOS 8.0+

## Declaration

```swift
class NINearbyAccessoryConfiguration
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Overview

Use this class to interact with a third-party accessory that you partner with or develop.

For an example app that demonstrates this configuration, see [`Implementing spatial interactions with third-party accessories`](implementing-spatial-interactions-with-third-party-accessories.md).

##### Discover the Accessory and Create a Configuration

To begin the interaction, your app discovers the nearby accessory using a technology you choose — like [`Core Bluetooth`](https://developer.apple.com/documentation/CoreBluetooth), the local network, or a secure internet connection — and establishes a two-way data link.

Over the data link, the accessory sends your app configuration data for this property’s [`init(data:)`](ninearbyaccessoryconfiguration/init(data:).md) initializer. The accessory formats the data according to the [`Ultra Wideband (UWB) third-party device specification`](https://developer.apple.comhttps://developer.apple.com/nearby-interaction/specification).

##### Enable Background Interaction for Bluetooth Accessories

In iOS 16, third-party UWB accessories paired to the device through Bluetooth can interact with your app while it’s in the background. This enables a new class of hands-free experiences. For example, the user’s phone can be in their pocket and prompt an eBike to power on when mounted, or prompt lights to turn on and music to play as the user enters a room.

To enable background interaction:

- The accessory implements the Bluetooth requirements described in the [`Ultra Wideband (UWB) third-party device specification`](https://developer.apple.comhttps://developer.apple.com/nearby-interaction/specification).
- The app connects and pairs to the accessory using [`Core Bluetooth`](https://developer.apple.com/documentation/CoreBluetooth).
- The app calls the [`init(accessoryData:bluetoothPeerIdentifier:)`](ninearbyaccessoryconfiguration/init(accessorydata:bluetoothpeeridentifier:).md) initializer and passes in the accessory’s Bluetooth identifier.

##### Start a Session and Share Configuration Data

To start a session, the app creates an [`NISession`](nisession.md) instance and passes an instance of this class into the session’s [`run(_:)`](nisession/run(_:).md) function. After your app sets the session [`delegate`](nisession/delegate.md), the system invokes the delegate’s [`session(_:didGenerateShareableConfigurationData:for:)`](nisessiondelegate/session(_:didgenerateshareableconfigurationdata:for:).md) callback and provides your device’s configuration data.

Over the data link, your app sends your device’s configuration data to the accessory, which enables the two devices to start receiving location updates. When the system gathers location updates for the accessory, Nearby Interaction calls your delegate’s [`session(_:didUpdate:)`](nisessiondelegate/session(_:didupdate:).md) implementation. To match [`distance`](ninearbyobject/distance-676dm.md) updates that your app receives through [`session(_:didUpdate:)`](nisessiondelegate/session(_:didupdate:).md) with the accessory, compare the argument object’s discovery token with the value of this property’s [`accessoryDiscoveryToken`](ninearbyaccessoryconfiguration/accessorydiscoverytoken.md).

##### Enable Precision Finding for Stationary Objects

In iOS 16, you can combine the visual-spatial power of ARKit with the radio sensitivity of the Ultra Wideband (UWB) chip to locate stationary nearby objects with considerable precision. To do that, set [`isCameraAssistanceEnabled`](ninearbyaccessoryconfiguration/iscameraassistanceenabled.md) to `true` and optionally provide the interaction session with an [`ARSession`](https://developer.apple.com/documentation/ARKit/ARSession) instance through [`setARSession(_:)`](nisession/setarsession(_:).md) before running the session. Together, the UWB chip and ARKit’s assistance enable Nearby Interaction to provide the same Precision Finding capabilities present in AirTag.

## Topics

### Creating a configuration
- [init(data: Data) throws](ninearbyaccessoryconfiguration/init(data:).md)
  Creates a configuration for interaction between iPhone and third-party accessories.
- [init(accessoryData: Data, bluetoothPeerIdentifier: UUID) throws](ninearbyaccessoryconfiguration/init(accessorydata:bluetoothpeeridentifier:).md)
  Creates a configuration for an accessory with the given Bluetooth peer identifier.
### Identifying the peer
- [var accessoryDiscoveryToken: NIDiscoveryToken](ninearbyaccessoryconfiguration/accessorydiscoverytoken.md)
  An identifier for the accessory in a session.
### Enabling Camera Assistance
- [var isCameraAssistanceEnabled: Bool](ninearbyaccessoryconfiguration/iscameraassistanceenabled.md)
  A Boolean value that combines the spatial awareness of ARKit with Nearby Interaction to improve the accuracy of a nearby object’s position.

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

- [Implementing spatial interactions with third-party accessories](implementing-spatial-interactions-with-third-party-accessories.md)
  Establish a connection with a nearby accessory to receive periodic measurements of its distance from the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyaccessoryconfiguration)*