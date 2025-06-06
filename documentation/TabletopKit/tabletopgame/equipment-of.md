# equipment(of:)

**Framework**: TabletopKit  
**Kind**: method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func equipment<E>(of type: E.Type) -> [E] where E : Equipment
```

## See Also

- [var equipment: [any Equipment]](tabletopgame/equipment.md)
- [var equipmentIDs: [EquipmentIdentifier]](tabletopgame/equipmentids.md)
- [func equipment(matching: EquipmentIdentifier) -> (any Equipment)?](tabletopgame/equipment(matching:).md)
- [func equipment<E>(of: E.Type, forEntity: Entity) -> E?](tabletopgame/equipment(of:forentity:).md)
  Retrieves the specified equipment type associated with an entity if it exists.
- [func equipment<E>(of: E.Type, matching: EquipmentIdentifier) -> E?](tabletopgame/equipment(of:matching:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/equipment(of:))*