# ObjectTrackingProvider.TrackingConfiguration

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

Parameters for changing object-tracking behavior.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TrackingConfiguration
```

#### Overview

Your app needs to include the [`Object-tracking parameter adjustment`](../../BundleResources/entitlements/com.apple.developer.arkit.object-tracking-parameter-adjustment.allow.md) entitlement to modify the tracking configuration; otherwise, it has no effect.

## Topics

### Creating a tracking configuration
- [init()](./trackingconfiguration-swift.struct/init%28%29.md)
  Creates a tracking configuration.
### Inspecting a tracking configuration
- [var detectionRate: Float](./trackingconfiguration-swift.struct/detectionrate.md)
  The frequency at which object detection runs, in Hz.
- [var maximumInstancesPerReferenceObject: Int](./trackingconfiguration-swift.struct/maximuminstancesperreferenceobject.md)
  The maximum number of instances of each reference object type to allow tracking at once.
- [var maximumTrackableInstances: Int](./trackingconfiguration-swift.struct/maximumtrackableinstances.md)
  The total number of object instances that you can track at the same time.
- [var movingObjectTrackingRate: Float](./trackingconfiguration-swift.struct/movingobjecttrackingrate.md)
  The frequency at which object tracking runs for moving objects, in Hz.
- [var stationaryObjectTrackingRate: Float](./trackingconfiguration-swift.struct/stationaryobjecttrackingrate.md)
  The frequency at which object tracking runs for stationary objects, in Hz.
### Instance Properties
- [var description: String](./trackingconfiguration-swift.struct/description.md)
  A textual representation of this tracking configuration.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)

## See Also

### Configuring object-tracking
- [var trackingConfiguration: ObjectTrackingProvider.TrackingConfiguration](./trackingconfiguration-swift.property.md)
  Returns the current parameters that are being used to configure object tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objecttrackingprovider/trackingconfiguration-swift.struct)*