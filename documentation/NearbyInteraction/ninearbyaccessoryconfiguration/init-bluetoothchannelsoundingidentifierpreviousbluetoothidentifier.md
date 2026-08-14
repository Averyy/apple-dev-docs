# init(bluetoothChannelSoundingIdentifier:previousBluetoothIdentifier:)

**Framework**: Nearby Interaction  
**Kind**: init

Initializes a configuration for Bluetooth Channel Sounding ranging with an accessory.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(bluetoothChannelSoundingIdentifier bluetoothIdentifier: UUID, previousBluetoothIdentifier: UUID?)
```

#### Discussion

Bluetooth Channel Sounding is a Bluetooth 6.0 specification ranging strategy that measure distance between iPhone and a paired accessory over a standard Bluetooth connection without requiring dedicated Ultra Wideband hardware.

Use this initializer to create an accessory configuration that implements Bluetooth Channel Sounding. Call [`supportsBluetoothChannelSounding`](nidevicecapability/supportsbluetoothchannelsounding.md) before running a session to ensure device support, and pair your accessory with [`AccessorySetupKit`](https://developer.apple.com/documentation/accessorysetupkit); the Nearby Interaction framework only supports Bluetooth Channel Sounding with accessories paired through [`AccessorySetupKit`](https://developer.apple.com/documentation/accessorysetupkit).

##### Handle Reconnections

When reconnecting to an accessory where the Bluetooth identifier can change, provide the previous identifier using the `previousBluetoothIdentifier` parameter. This allows the session to maintain internal state continuity across reconnections. For initial connections, pass `nil` for this parameter.

```swift
// Initial connection.
let config = NINearbyAccessoryConfiguration(
    bluetoothChannelSoundingIdentifier: btcsIdentifier,
    previousBluetoothIdentifier: nil
)
session.run(config)

// Reconnection with a new identifier.
let reconnectConfig = NINearbyAccessoryConfiguration(
    bluetoothChannelSoundingIdentifier: newBtcsIdentifier,
    previousBluetoothIdentifier: previousBtcsIdentifier
)
session.run(reconnectConfig)
```

## Parameters

- `bluetoothIdentifier`: An identifier that the session uses to establish the Bluetooth connection with the accessory. This identifier originates from the Bluetooth Channel Sounding protocol.
- `previousBluetoothIdentifier`: An optional previous Bluetooth identifier for reconnection scenarios.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyaccessoryconfiguration/init(bluetoothchannelsoundingidentifier:previousbluetoothidentifier:))*