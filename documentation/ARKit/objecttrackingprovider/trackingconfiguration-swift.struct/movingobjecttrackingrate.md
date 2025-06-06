# movingObjectTrackingRate

**Framework**: ARKit  
**Kind**: property

The frequency at which object tracking runs for moving objects, in Hz.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var movingObjectTrackingRate: Float
```

#### Discussion

The framework clamps this to between `0` and `30` Hz.

## See Also

- [var detectionRate: Float](objecttrackingprovider/trackingconfiguration-swift.struct/detectionrate.md)
  The frequency at which object detection runs, in Hz.
- [var maximumInstancesPerReferenceObject: Int](objecttrackingprovider/trackingconfiguration-swift.struct/maximuminstancesperreferenceobject.md)
  The maximum number of instances of each reference object type to allow tracking at once.
- [var maximumTrackableInstances: Int](objecttrackingprovider/trackingconfiguration-swift.struct/maximumtrackableinstances.md)
  The total number of object instances that you can track at the same time.
- [var stationaryObjectTrackingRate: Float](objecttrackingprovider/trackingconfiguration-swift.struct/stationaryobjecttrackingrate.md)
  The frequency at which object tracking runs for stationary objects, in Hz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objecttrackingprovider/trackingconfiguration-swift.struct/movingobjecttrackingrate)*