# hovering

**Framework**: TabletopKit  
**Kind**: property

The current destination for the equipment, if the interaction were to end now. `nil` if no destination is currently available.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var hovering: TabletopInteraction.Destination?
```

## See Also

- [let controlledEquipmentPose: EquipmentPose3D](tablecursor/controlledequipmentpose.md)
  The identifier of the equipment and the pose of the equipment in table space. NOTE: the equipment pose returned here does not include the resting orientation, similarly to the `pose` and `initialPose`in `TabletopInteraction.Value`. This is unlike the `pose` returned in `TableVisualState`, which does include resting orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablecursor/hovering)*