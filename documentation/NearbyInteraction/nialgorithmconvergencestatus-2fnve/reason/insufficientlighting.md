# insufficientLighting

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Type Property

Indicates that the camera needs to view the physical environment under better lighting conditions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
static let insufficientLighting: NIAlgorithmConvergenceStatus.Reason
```

#### Discussion

Coach the user to resolve the issue, such as by presenting text that asks the user to turn on the lights.

This reason prevents a nearby object from providing a [`horizontalAngle`](../../ninearbyobject/horizontalangle-hsg.md) and [`verticalDirectionEstimate`](../../ninearbyobject/verticaldirectionestimate-swift.property.md).

## See Also

### Interpreting the convergence status reason
- [static let insufficientMovement: NIAlgorithmConvergenceStatus.Reason](./insufficientmovement.md)
  Indicates that the device needs to move from its current position in the physical environment.
- [static let insufficientHorizontalSweep: NIAlgorithmConvergenceStatus.Reason](./insufficienthorizontalsweep.md)
  Indicates that the device needs more horizontal motion.
- [static let insufficientVerticalSweep: NIAlgorithmConvergenceStatus.Reason](./insufficientverticalsweep.md)
  Indicates that the device needs more vertical motion.
- [static let insufficientSignalStrength: NIAlgorithmConvergenceStatus.Reason](./insufficientsignalstrength.md)
  Indicates that the users might be too far apart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fnve/reason/insufficientlighting)*