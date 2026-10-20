# equipmentIDs

**Framework**: TabletopKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var equipmentIDs: [EquipmentIdentifier] { get }
```

## See Also

### Adding equipment to the game
- [var equipment: [any Equipment]](./equipment.md)
- [func equipment(matching: EquipmentIdentifier) -> (any Equipment)?](./equipment%28matching%29.md)
- [func equipment<E>(of: E.Type) -> [E]](./equipment%28of%29.md)
- [func equipment<E>(of: E.Type, forEntity: Entity) -> E?](./equipment%28of,forentity%29.md)
  Retrieves the specified equipment type associated with an entity if it exists.
- [func equipment<E>(of: E.Type, matching: EquipmentIdentifier) -> E?](./equipment%28of,matching%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/equipmentids)*