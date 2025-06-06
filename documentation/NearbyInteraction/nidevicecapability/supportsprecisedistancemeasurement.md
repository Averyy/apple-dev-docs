# supportsPreciseDistanceMeasurement

**Framework**: Nearby Interaction  
**Kind**: property  
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

#### Discussion

If [`false`](https://developer.apple.com/documentation/swift/false), then the device doesn’t support Nearby Interaction.

This property is functionally equivalent to the deprecated [`isSupported`](nisession/issupported.md).

## See Also

- [var supportsDirectionMeasurement: Bool](nidevicecapability/supportsdirectionmeasurement.md)
  A Boolean value that indicates whether the device produces instantaneous direction measurements to nearby objects.
- [var supportsCameraAssistance: Bool](nidevicecapability/supportscameraassistance.md)
  A Boolean value that indicates whether the device can leverage ARKit to improve interaction.
- [var supportsExtendedDistanceMeasurement: Bool](nidevicecapability/supportsextendeddistancemeasurement.md)
  A Boolean value that indicates whether this device supports extended distance measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidevicecapability/supportsprecisedistancemeasurement)*