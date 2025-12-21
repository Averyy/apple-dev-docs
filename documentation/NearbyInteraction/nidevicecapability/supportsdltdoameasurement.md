# supportsDLTDOAMeasurement

**Framework**: Nearby Interaction  
**Kind**: property  
**Required**: Yes

A property that indicates if the device supports Downlink Time-Difference-of-Arrival ranging.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var supportsDLTDOAMeasurement: Bool { get }
```

#### Discussion

Only create a [`NIDLTDOAConfiguration`](nidltdoaconfiguration.md) instance if the value of this property is `true`.

## See Also

- [var supportsPreciseDistanceMeasurement: Bool](nidevicecapability/supportsprecisedistancemeasurement.md)
  A Boolean value that indicates whether the device produces precise distance measurements to nearby objects.
- [var supportsDirectionMeasurement: Bool](nidevicecapability/supportsdirectionmeasurement.md)
  A Boolean value that indicates whether the device produces instantaneous direction measurements to nearby objects.
- [var supportsCameraAssistance: Bool](nidevicecapability/supportscameraassistance.md)
  A Boolean value that indicates whether the device can leverage ARKit to improve interaction.
- [var supportsExtendedDistanceMeasurement: Bool](nidevicecapability/supportsextendeddistancemeasurement.md)
  A Boolean value that indicates whether this device supports extended distance measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidevicecapability/supportsdltdoameasurement)*