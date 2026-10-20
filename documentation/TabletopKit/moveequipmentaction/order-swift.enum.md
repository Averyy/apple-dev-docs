# MoveEquipmentAction.Order

**Framework**: TabletopKit  
**Kind**: enum  
**Role**: Enumeration

The possible orders of equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum Order
```

## Topics

### Orders
- [MoveEquipmentAction.Order.first](./order-swift.enum/first.md)
  Inserts the equipment at the beginning of the list
- [MoveEquipmentAction.Order.last](./order-swift.enum/last.md)
  Inserts the equipment at the end of the list
- [MoveEquipmentAction.Order.before(_:)](./order-swift.enum/before%28_%29.md)
  Inserts the equipment before the specified equipment identifier.
- [MoveEquipmentAction.Order.after(_:)](./order-swift.enum/after%28_%29.md)
  Inserts the equipment after the specified equipment identifier.
- [MoveEquipmentAction.Order.atIndex(_:)](./order-swift.enum/atindex%28_%29.md)
  Inserts the equipment at a specific location Note: the equipment is inserted at a undefined location if the index provided is not valid

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the equipment in the action
- [var equipmentID: EquipmentIdentifier](./equipmentid.md)
  The ID of the equipment being moved.
- [var parentID: EquipmentIdentifier](./parentid.md)
  The equipment ID the moved equipment is being grouped under
- [var playerID: Player.ID?](./playerid.md)
  The ID of the player who is moving the equipment.
- [var order: MoveEquipmentAction.Order?](./order-swift.property.md)
  The order in which the equipment should be inserted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/moveequipmentaction/order-swift.enum)*