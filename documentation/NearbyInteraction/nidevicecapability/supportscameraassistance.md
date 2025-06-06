# supportsCameraAssistance

**Framework**: Nearbyinteraction  
**Kind**: property  
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

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Discussion

For more on Camera Assistance, see [`isCameraAssistanceEnabled`](ninearbypeerconfiguration/iscameraassistanceenabled.md).

> **Note**:  Apple Watch doesn’t support Camera Assistance.

## See Also

- [var supportsPreciseDistanceMeasurement: Bool](nidevicecapability/supportsprecisedistancemeasurement.md)
  A Boolean value that indicates whether the device produces precise distance measurements to nearby objects.
- [var supportsDirectionMeasurement: Bool](nidevicecapability/supportsdirectionmeasurement.md)
  A Boolean value that indicates whether the device produces instantaneous direction measurements to nearby objects.
- [var supportsExtendedDistanceMeasurement: Bool](nidevicecapability/supportsextendeddistancemeasurement.md)
  A Boolean value that indicates whether this device supports extended distance measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidevicecapability/supportscameraassistance)*