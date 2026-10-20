# equipment(of:forEntity:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

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

### Adding equipment to the game
- [var equipment: [any Equipment]](./equipment.md)
- [var equipmentIDs: [EquipmentIdentifier]](./equipmentids.md)
- [func equipment(matching: EquipmentIdentifier) -> (any Equipment)?](./equipment%28matching%29.md)
- [func equipment<E>(of: E.Type) -> [E]](./equipment%28of%29.md)
- [func equipment<E>(of: E.Type, matching: EquipmentIdentifier) -> E?](./equipment%28of,matching%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/equipment(of:forentity:))*