# supportsDLTDOAMeasurement

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A property that indicates if the device supports Downlink Time-Difference-of-Arrival ranging.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var supportsDLTDOAMeasurement: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL supportsDLTDOAMeasurement;
```

#### Discussion

Only create a [`NIDLTDOAConfiguration`](../nidltdoaconfiguration.md) instance if the value of this property is `true`.

## See Also

### Checking session features
- [var supportsPreciseDistanceMeasurement: Bool](./supportsprecisedistancemeasurement.md)
  A Boolean value that indicates whether the device produces precise distance measurements to nearby objects.
- [var supportsDirectionMeasurement: Bool](./supportsdirectionmeasurement.md)
  A Boolean value that indicates whether the device produces instantaneous direction measurements to nearby objects.
- [var supportsCameraAssistance: Bool](./supportscameraassistance.md)
  A Boolean value that indicates whether the device can leverage ARKit to improve interaction.
- [var supportsExtendedDistanceMeasurement: Bool](./supportsextendeddistancemeasurement.md)
  A Boolean value that indicates whether this device supports extended distance measurement.
- [var supportsBluetoothChannelSounding: Bool](./supportsbluetoothchannelsounding.md)
  A Boolean value that indicates whether the device supports distance measurements over a Bluetooth connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidevicecapability/supportsdltdoameasurement)*