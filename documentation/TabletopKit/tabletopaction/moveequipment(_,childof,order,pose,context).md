# moveEquipment(_:childOf:order:pose:context:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func moveEquipment(_ equipment: some Equipment, childOf parent: any Equipment, order: MoveEquipmentAction.Order? = nil, pose: TableVisualState.Pose2D? = nil, context: UInt64 = 0) -> Self
```

Available when `Self` is `MoveEquipmentAction`.

## See Also

### Moving equipment
- [static func moveEquipment(matching: EquipmentIdentifier, childOf: EquipmentIdentifier, order: MoveEquipmentAction.Order?, pose: TableVisualState.Pose2D?, context: UInt64) -> Self](./moveequipment%28matching,childof,order,pose,context%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopaction/moveequipment(_:childof:order:pose:context:))*