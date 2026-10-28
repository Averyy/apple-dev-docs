# supportsCameraAssistance

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the device can leverage ARKit to improve interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
var supportsCameraAssistance: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL supportsCameraAssistance;
```

## Mentions

- [Initiating and maintaining a session](../initiating-and-maintaining-a-session.md)

## Discussion

For more on Camera Assistance, see [`isCameraAssistanceEnabled`](../ninearbypeerconfiguration/iscameraassistanceenabled.md).

> **Note**:  Apple Watch doesn’t support Camera Assistance.

## See Also

### Checking session features
- [var supportsPreciseDistanceMeasurement: Bool](./supportsprecisedistancemeasurement.md)
  A Boolean value that indicates whether the device produces precise distance measurements to nearby objects.
- [var supportsDirectionMeasurement: Bool](./supportsdirectionmeasurement.md)
  A Boolean value that indicates whether the device produces instantaneous direction measurements to nearby objects.
- [var supportsExtendedDistanceMeasurement: Bool](./supportsextendeddistancemeasurement.md)
  A Boolean value that indicates whether this device supports extended distance measurement.
- [var supportsDLTDOAMeasurement: Bool](./supportsdltdoameasurement.md)
  A property that indicates if the device supports Downlink Time-Difference-of-Arrival ranging.
- [var supportsBluetoothChannelSounding: Bool](./supportsbluetoothchannelsounding.md)
  A Boolean value that indicates whether the device supports distance measurements over a Bluetooth connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidevicecapability/supportscameraassistance)*