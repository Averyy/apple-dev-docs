# init(accessoryData:bluetoothPeerIdentifier:)

**Framework**: Nearby Interaction  
**Kind**: init

Creates a configuration for an accessory with the given Bluetooth peer identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
init(accessoryData: Data, bluetoothPeerIdentifier identifier: UUID) throws
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Discussion

Use this initializer when your app interacts with a Bluetooth accessory that’s paired to the device to enable interaction while your app is in the background.

## Parameters

- `accessoryData`: The accessory’s configuration data formatted to the  .
- `identifier`: The accessory’s Bluetooth peer identifier. For more information, see    .

## See Also

- [init(data: Data) throws](ninearbyaccessoryconfiguration/init(data:).md)
  Creates a configuration for interaction between iPhone and third-party accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyaccessoryconfiguration/init(accessorydata:bluetoothpeeridentifier:))*