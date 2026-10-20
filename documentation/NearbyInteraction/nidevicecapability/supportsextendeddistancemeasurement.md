# supportsExtendedDistanceMeasurement

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether this device supports extended distance measurement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- watchOS 10.0+

## Declaration

```swift
var supportsExtendedDistanceMeasurement: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL supportsExtendedDistanceMeasurement;
```

## See Also

### Checking session features
- [var supportsPreciseDistanceMeasurement: Bool](./supportsprecisedistancemeasurement.md)
  A Boolean value that indicates whether the device produces precise distance measurements to nearby objects.
- [var supportsDirectionMeasurement: Bool](./supportsdirectionmeasurement.md)
  A Boolean value that indicates whether the device produces instantaneous direction measurements to nearby objects.
- [var supportsCameraAssistance: Bool](./supportscameraassistance.md)
  A Boolean value that indicates whether the device can leverage ARKit to improve interaction.
- [var supportsDLTDOAMeasurement: Bool](./supportsdltdoameasurement.md)
  A property that indicates if the device supports Downlink Time-Difference-of-Arrival ranging.
- [var supportsBluetoothChannelSounding: Bool](./supportsbluetoothchannelsounding.md)
  A Boolean value that indicates whether the device supports distance measurements over a Bluetooth connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidevicecapability/supportsextendeddistancemeasurement)*