# supportsBluetoothChannelSounding

**Framework**: Nearby Interaction  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the device supports distance measurements over a Bluetooth connection.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var supportsBluetoothChannelSounding: Bool { get }
```

#### Discussion

Bluetooth Channel Sounding is a Bluetooth 6.0 specification ranging strategy that relies on a Bluetooth connection to measure distance between iPhone and a paired accessory.

Check this property before using Bluetooth Channel Sounding ranging to ensure the device has the required hardware capabilities. Running a Bluetooth Channel Sounding session on an unsupported device invalidates the session with an error.

To use Bluetooth Channel Sounding,

- Pair your accessory with [`AccessorySetupKit`](https://developer.apple.com/documentation/accessorysetupkit); the Nearby Interaction framework only supports Bluetooth Channel Sounding with accessories paired through [`AccessorySetupKit`](https://developer.apple.com/documentation/accessorysetupkit).
- Instantiate an [`NINearbyAccessoryConfiguration`](ninearbyaccessoryconfiguration.md) using the [`init(bluetoothChannelSoundingIdentifier:previousBluetoothIdentifier:)`](ninearbyaccessoryconfiguration/init(bluetoothchannelsoundingidentifier:previousbluetoothidentifier:).md) initializer:

```swift
guard NISession.deviceCapabilities.supportsBluetoothChannelSounding else {
    print("Device doesn't support Bluetooth Channel Sounding.")
    return
}

// Create a configuration for Bluetooth Channel Sounding ranging.
let config = NINearbyAccessoryConfiguration(
    bluetoothChannelSoundingIdentifier: identifier,
    previousBluetoothIdentifier: nil
)
session.run(config)
```

## See Also

- [var supportsPreciseDistanceMeasurement: Bool](nidevicecapability/supportsprecisedistancemeasurement.md)
  A Boolean value that indicates whether the device produces precise distance measurements to nearby objects.
- [var supportsDirectionMeasurement: Bool](nidevicecapability/supportsdirectionmeasurement.md)
  A Boolean value that indicates whether the device produces instantaneous direction measurements to nearby objects.
- [var supportsCameraAssistance: Bool](nidevicecapability/supportscameraassistance.md)
  A Boolean value that indicates whether the device can leverage ARKit to improve interaction.
- [var supportsExtendedDistanceMeasurement: Bool](nidevicecapability/supportsextendeddistancemeasurement.md)
  A Boolean value that indicates whether this device supports extended distance measurement.
- [var supportsDLTDOAMeasurement: Bool](nidevicecapability/supportsdltdoameasurement.md)
  A property that indicates if the device supports Downlink Time-Difference-of-Arrival ranging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidevicecapability/supportsbluetoothchannelsounding)*