# equipment(of:forEntity:)

**Framework**: TabletopKit  
**Kind**: method

Retrieves the specified equipment type associated with an entity if it exists.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func equipment<E>(of type: E.Type, forEntity entity: Entity) -> E? where E : EntityEquipment
```

#### Return Value

The equipment associated with the entity if it exists; otherwise, `nil`.

#### Discussion

You can use this method to create custom interactions.

## Parameters

- `type`: The type of equipment to retrieve.
- `entity`: The entity that’s associated with the equipment type you want to find.

## See Also

- [var equipment: [any Equipment]](tabletopgame/equipment.md)
- [var equipmentIDs: [EquipmentIdentifier]](tabletopgame/equipmentids.md)
- [func equipment(matching: EquipmentIdentifier) -> (any Equipment)?](tabletopgame/equipment(matching:).md)
- [func equipment<E>(of: E.Type) -> [E]](tabletopgame/equipment(of:).md)
- [func equipment<E>(of: E.Type, matching: EquipmentIdentifier) -> E?](tabletopgame/equipment(of:matching:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/equipment(of:forentity:))*