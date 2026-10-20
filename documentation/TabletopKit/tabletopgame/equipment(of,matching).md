# equipment(of:matching:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func equipment<E>(of type: E.Type, matching id: EquipmentIdentifier) -> E? where E : Equipment
```

## See Also

### Adding equipment to the game
- [var equipment: [any Equipment]](./equipment.md)
- [var equipmentIDs: [EquipmentIdentifier]](./equipmentids.md)
- [func equipment(matching: EquipmentIdentifier) -> (any Equipment)?](./equipment%28matching%29.md)
- [func equipment<E>(of: E.Type) -> [E]](./equipment%28of%29.md)
- [func equipment<E>(of: E.Type, forEntity: Entity) -> E?](./equipment%28of,forentity%29.md)
  Retrieves the specified equipment type associated with an entity if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/equipment(of:matching:))*