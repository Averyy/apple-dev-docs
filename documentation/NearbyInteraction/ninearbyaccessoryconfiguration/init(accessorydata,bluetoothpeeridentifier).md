# init(accessoryData:bluetoothPeerIdentifier:)

**Framework**: Nearby Interaction  
**Kind**: init  
**Role**: Initializer

Creates a configuration for an accessory with the given Bluetooth peer identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
init(accessoryData: Data, bluetoothPeerIdentifier identifier: UUID) throws
```

```objc
- (instancetype) initWithAccessoryData:(NSData *) accessoryData bluetoothPeerIdentifier:(NSUUID *) identifier error:(NSError **) error;
```

## Mentions

- [Initiating and maintaining a session](../initiating-and-maintaining-a-session.md)

#### Discussion

Use this initializer when your app interacts with a Bluetooth accessory that’s paired to the device to enable interaction while your app is in the background.

## Parameters

- `accessoryData`: The accessory’s configuration data formatted to the [Ultra Wideband (UWB) third-party device specification](https://developer.apple.com/nearby-interaction).
- `identifier`: The accessory’s Bluetooth peer identifier. For more information, see [`CBPeer`](../../CoreBluetooth/cbpeer.md) [`identifier`](../../CoreBluetooth/cbpeer/identifier.md).

## See Also

### Creating a configuration for UWB accessories
- [init(data: Data) throws](./init%28data%29.md)
  Creates a configuration for interaction between iPhone and third-party accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyaccessoryconfiguration/init(accessorydata:bluetoothpeeridentifier:))*