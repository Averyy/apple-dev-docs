# controlledEquipmentPose

**Framework**: TabletopKit  
**Kind**: property

The identifier of the equipment and the pose of the equipment in table space. NOTE: the equipment pose returned here does not include the resting orientation, similarly to the `pose` and `initialPose`in `TabletopInteraction.Value`. This is unlike the `pose` returned in `TableVisualState`, which does include resting orientation.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
let controlledEquipmentPose: EquipmentPose3D
```

## See Also

- [var hovering: TabletopInteraction.Destination?](tablecursor/hovering.md)
  The current destination for the equipment, if the interaction were to end now. `nil` if no destination is currently available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablecursor/controlledequipmentpose)*