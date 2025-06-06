# insufficientVerticalSweep

**Framework**: Nearby Interaction  
**Kind**: property

Indicates that the device needs more vertical motion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
static let insufficientVerticalSweep: NIAlgorithmConvergenceStatus.Reason
```

#### Discussion

Coach the user to resolve the issue, such as by presenting text that asks the user to move the device in a vertical direction.

This reason may prevent a nearby object from providing a [`verticalDirectionEstimate`](ninearbyobject/verticaldirectionestimate-swift.property.md). This reason doesn’t effect the [`horizontalAngle`](ninearbyobject/horizontalangle-hsg.md) property.

## See Also

- [static let insufficientMovement: NIAlgorithmConvergenceStatus.Reason](nialgorithmconvergencestatus-2fnve/reason/insufficientmovement.md)
  Indicates that the device needs to move from its current position in the physical environment.
- [static let insufficientHorizontalSweep: NIAlgorithmConvergenceStatus.Reason](nialgorithmconvergencestatus-2fnve/reason/insufficienthorizontalsweep.md)
  Indicates that the device needs more horizontal motion.
- [static let insufficientLighting: NIAlgorithmConvergenceStatus.Reason](nialgorithmconvergencestatus-2fnve/reason/insufficientlighting.md)
  Indicates that the camera needs to view the physical environment under better lighting conditions.
- [static let insufficientSignalStrength: NIAlgorithmConvergenceStatus.Reason](nialgorithmconvergencestatus-2fnve/reason/insufficientsignalstrength.md)
  Indicates that the users might be too far apart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fnve/reason/insufficientverticalsweep)*