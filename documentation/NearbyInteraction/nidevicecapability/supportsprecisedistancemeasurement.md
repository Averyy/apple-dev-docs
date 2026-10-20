# supportsPreciseDistanceMeasurement

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the device produces precise distance measurements to nearby objects.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
var supportsPreciseDistanceMeasurement: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL supportsPreciseDistanceMeasurement;
```

#### Discussion

If [`false`](../../Swift/false.md), then the device doesn’t support Nearby Interaction.

This property is functionally equivalent to the deprecated [`isSupported`](../nisession/issupported.md).

## See Also

### Checking session features
- [var supportsDirectionMeasurement: Bool](./supportsdirectionmeasurement.md)
  A Boolean value that indicates whether the device produces instantaneous direction measurements to nearby objects.
- [var supportsCameraAssistance: Bool](./supportscameraassistance.md)
  A Boolean value that indicates whether the device can leverage ARKit to improve interaction.
- [var supportsExtendedDistanceMeasurement: Bool](./supportsextendeddistancemeasurement.md)
  A Boolean value that indicates whether this device supports extended distance measurement.
- [var supportsDLTDOAMeasurement: Bool](./supportsdltdoameasurement.md)
  A property that indicates if the device supports Downlink Time-Difference-of-Arrival ranging.
- [var supportsBluetoothChannelSounding: Bool](./supportsbluetoothchannelsounding.md)
  A Boolean value that indicates whether the device supports distance measurements over a Bluetooth connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidevicecapability/supportsprecisedistancemeasurement)*