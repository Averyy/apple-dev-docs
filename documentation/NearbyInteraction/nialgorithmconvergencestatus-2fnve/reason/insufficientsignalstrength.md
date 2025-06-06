# insufficientSignalStrength

**Framework**: Nearby Interaction  
**Kind**: property

Indicates that the users might be too far apart.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
static let insufficientSignalStrength: NIAlgorithmConvergenceStatus.Reason
```

#### Discussion

Coach the user to resolve the issue, such as by presenting text that instructs the user to move closer to the nearby peer or object.

## See Also

- [static let insufficientMovement: NIAlgorithmConvergenceStatus.Reason](nialgorithmconvergencestatus-2fnve/reason/insufficientmovement.md)
  Indicates that the device needs to move from its current position in the physical environment.
- [static let insufficientHorizontalSweep: NIAlgorithmConvergenceStatus.Reason](nialgorithmconvergencestatus-2fnve/reason/insufficienthorizontalsweep.md)
  Indicates that the device needs more horizontal motion.
- [static let insufficientVerticalSweep: NIAlgorithmConvergenceStatus.Reason](nialgorithmconvergencestatus-2fnve/reason/insufficientverticalsweep.md)
  Indicates that the device needs more vertical motion.
- [static let insufficientLighting: NIAlgorithmConvergenceStatus.Reason](nialgorithmconvergencestatus-2fnve/reason/insufficientlighting.md)
  Indicates that the camera needs to view the physical environment under better lighting conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fnve/reason/insufficientsignalstrength)*