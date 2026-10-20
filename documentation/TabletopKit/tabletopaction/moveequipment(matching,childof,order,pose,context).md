# moveEquipment(matching:childOf:order:pose:context:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func moveEquipment(matching equipmentID: EquipmentIdentifier, childOf parentID: EquipmentIdentifier, order: MoveEquipmentAction.Order? = nil, pose: TableVisualState.Pose2D? = nil, context: UInt64 = 0) -> Self
```

Available when `Self` is `MoveEquipmentAction`.

## See Also

### Moving equipment
- [static func moveEquipment(some Equipment, childOf: any Equipment, order: MoveEquipmentAction.Order?, pose: TableVisualState.Pose2D?, context: UInt64) -> Self](./moveequipment%28_,childof,order,pose,context%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopaction/moveequipment(matching:childof:order:pose:context:))*