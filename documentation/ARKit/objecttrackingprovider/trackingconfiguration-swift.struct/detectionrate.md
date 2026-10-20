# detectionRate

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The frequency at which object detection runs, in Hz.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var detectionRate: Float
```

#### Discussion

The framework clamps this value to between `0` and `30` Hz.

## See Also

### Inspecting a tracking configuration
- [var maximumInstancesPerReferenceObject: Int](./maximuminstancesperreferenceobject.md)
  The maximum number of instances of each reference object type to allow tracking at once.
- [var maximumTrackableInstances: Int](./maximumtrackableinstances.md)
  The total number of object instances that you can track at the same time.
- [var movingObjectTrackingRate: Float](./movingobjecttrackingrate.md)
  The frequency at which object tracking runs for moving objects, in Hz.
- [var stationaryObjectTrackingRate: Float](./stationaryobjecttrackingrate.md)
  The frequency at which object tracking runs for stationary objects, in Hz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objecttrackingprovider/trackingconfiguration-swift.struct/detectionrate)*