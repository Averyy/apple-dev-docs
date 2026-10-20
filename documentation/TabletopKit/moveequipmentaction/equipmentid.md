# equipmentID

**Framework**: TabletopKit  
**Kind**: property  
**Role**: Instance Property

The ID of the equipment being moved.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var equipmentID: EquipmentIdentifier { get }
```

## See Also

### Getting the equipment in the action
- [var parentID: EquipmentIdentifier](./parentid.md)
  The equipment ID the moved equipment is being grouped under
- [var playerID: Player.ID?](./playerid.md)
  The ID of the player who is moving the equipment.
- [var order: MoveEquipmentAction.Order?](./order-swift.property.md)
  The order in which the equipment should be inserted.
- [MoveEquipmentAction.Order](./order-swift.enum.md)
  The possible orders of equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/moveequipmentaction/equipmentid)*