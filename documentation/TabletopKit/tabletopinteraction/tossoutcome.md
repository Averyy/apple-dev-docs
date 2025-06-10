# TabletopInteraction.TossOutcome

**Framework**: TabletopKit  
**Kind**: struct

An object representing the final outcome of tossing one equipment, as it appears at the end of its simulation.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct TossOutcome
```

## Topics

### Instance Properties
- [var id: EquipmentIdentifier](tabletopinteraction/tossoutcome/id.md)
  The identifier of the equipment that was tossed.
- [var pose: TableVisualState.Pose2D](tabletopinteraction/tossoutcome/pose.md)
  The final pose of the equipment at the end of the toss simulation, in table space.
- [var restingOrientation: Rotation3D](tabletopinteraction/tossoutcome/restingorientation.md)
  The final resting orientation of the equipment at the end of the toss simulation.
- [var tossableRepresentation: TossableRepresentation](tabletopinteraction/tossoutcome/tossablerepresentation.md)
  The tossable representation of the equipment that was tossed.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/tossoutcome)*