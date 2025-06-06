# NIDeviceCapability

**Framework**: Nearby Interaction  
**Kind**: protocol

An interface that adds Boolean values that indicate an interaction session feature support.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
protocol NIDeviceCapability
```

#### Overview

The [`NISession`](nisession.md) class property [`deviceCapabilities`](nisession/devicecapabilities.md) adopts this protocol. At runtime, inspect this property to determine the available features of an interaction session on the person’s device.

In a compatible iPad or iPhone app running in visionOS, the framework reports that all capabilities are unavailable.

## Topics

### Session features
- [var supportsPreciseDistanceMeasurement: Bool](nidevicecapability/supportsprecisedistancemeasurement.md)
  A Boolean value that indicates whether the device produces precise distance measurements to nearby objects.
- [var supportsDirectionMeasurement: Bool](nidevicecapability/supportsdirectionmeasurement.md)
  A Boolean value that indicates whether the device produces instantaneous direction measurements to nearby objects.
- [var supportsCameraAssistance: Bool](nidevicecapability/supportscameraassistance.md)
  A Boolean value that indicates whether the device can leverage ARKit to improve interaction.
- [var supportsExtendedDistanceMeasurement: Bool](nidevicecapability/supportsextendeddistancemeasurement.md)
  A Boolean value that indicates whether this device supports extended distance measurement.

## See Also

- [class var deviceCapabilities: any NIDeviceCapability](nisession/devicecapabilities.md)
  An object that communicates the device’s supported framework features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidevicecapability)*