# ObjectTrackingProvider.TrackingConfiguration

**Framework**: ARKit  
**Kind**: struct

Parameters for changing object-tracking behavior.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TrackingConfiguration
```

#### Overview

Your app needs to include the [`Object-tracking parameter adjustment`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.arkit.object-tracking-parameter-adjustment.allow) entitlement to modify the tracking configuration; otherwise, it has no effect.

## Topics

### Creating a tracking configuration
- [init()](objecttrackingprovider/trackingconfiguration-swift.struct/init.md)
  Creates a tracking configuration.
### Inspecting a tracking configuration
- [var detectionRate: Float](objecttrackingprovider/trackingconfiguration-swift.struct/detectionrate.md)
  The frequency at which object detection runs, in Hz.
- [var maximumInstancesPerReferenceObject: Int](objecttrackingprovider/trackingconfiguration-swift.struct/maximuminstancesperreferenceobject.md)
  The maximum number of instances of each reference object type to allow tracking at once.
- [var maximumTrackableInstances: Int](objecttrackingprovider/trackingconfiguration-swift.struct/maximumtrackableinstances.md)
  The total number of object instances that you can track at the same time.
- [var movingObjectTrackingRate: Float](objecttrackingprovider/trackingconfiguration-swift.struct/movingobjecttrackingrate.md)
  The frequency at which object tracking runs for moving objects, in Hz.
- [var stationaryObjectTrackingRate: Float](objecttrackingprovider/trackingconfiguration-swift.struct/stationaryobjecttrackingrate.md)
  The frequency at which object tracking runs for stationary objects, in Hz.
### Instance Properties
- [var description: String](objecttrackingprovider/trackingconfiguration-swift.struct/description.md)
  A textual representation of this tracking configuration.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [var trackingConfiguration: ObjectTrackingProvider.TrackingConfiguration](objecttrackingprovider/trackingconfiguration-swift.property.md)
  Returns the current parameters that are being used to configure object tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objecttrackingprovider/trackingconfiguration-swift.struct)*