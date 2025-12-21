# MoveEquipmentAction.Order

**Framework**: TabletopKit  
**Kind**: enum

The possible orders of equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum Order
```

## Topics

### Orders
- [MoveEquipmentAction.Order.first](moveequipmentaction/order-swift.enum/first.md)
  Inserts the equipment at the beginning of the list
- [MoveEquipmentAction.Order.last](moveequipmentaction/order-swift.enum/last.md)
  Inserts the equipment at the end of the list
- [MoveEquipmentAction.Order.before(_:)](moveequipmentaction/order-swift.enum/before(_:).md)
  Inserts the equipment before the specified equipment identifier.
- [MoveEquipmentAction.Order.after(_:)](moveequipmentaction/order-swift.enum/after(_:).md)
  Inserts the equipment after the specified equipment identifier.
- [MoveEquipmentAction.Order.atIndex(_:)](moveequipmentaction/order-swift.enum/atindex(_:).md)
  Inserts the equipment at a specific location Note: the equipment is inserted at a undefined location if the index provided is not valid

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var equipmentID: EquipmentIdentifier](moveequipmentaction/equipmentid.md)
  The ID of the equipment being moved.
- [var parentID: EquipmentIdentifier](moveequipmentaction/parentid.md)
  The equipment ID the moved equipment is being grouped under
- [var playerID: Player.ID?](moveequipmentaction/playerid.md)
  The ID of the player who is moving the equipment.
- [var order: MoveEquipmentAction.Order?](moveequipmentaction/order-swift.property.md)
  The order in which the equipment should be inserted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/moveequipmentaction/order-swift.enum)*