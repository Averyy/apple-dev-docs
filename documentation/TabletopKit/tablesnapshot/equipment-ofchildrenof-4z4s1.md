# equipment(of:childrenOf:)

**Framework**: TabletopKit  
**Kind**: method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func equipment<E>(of type: E.Type, childrenOf parent: some Equipment) -> [(E, E.State)] where E : Equipment
```

## See Also

- [func equipment<E>(of: E.Type) -> [(E, E.State)]](tablesnapshot/equipment(of:).md)
- [func equipment<E>(of: E.Type, childrenOf: EquipmentIdentifier) -> [(E, E.State)]](tablesnapshot/equipment(of:childrenof:)-5w137.md)
- [func equipment<E>(of: E.Type, matching: some Sequence<EquipmentIdentifier>) -> [(E, E.State)]](tablesnapshot/equipment(of:matching:)-7ai0c.md)
- [func equipment<E>(of: E.Type, matching: EquipmentIdentifier) -> (E, E.State)?](tablesnapshot/equipment(of:matching:)-8qve2.md)
- [func equipmentIDs() -> [EquipmentIdentifier]](tablesnapshot/equipmentids.md)
- [func equipmentIDs(childrenOf: some Equipment) -> [EquipmentIdentifier]](tablesnapshot/equipmentids(childrenof:)-432sk.md)
- [func equipmentIDs(childrenOf: EquipmentIdentifier) -> [EquipmentIdentifier]](tablesnapshot/equipmentids(childrenof:)-f1sp.md)
- [func state(matching: EquipmentIdentifier) -> (any EquipmentState)?](tablesnapshot/state(matching:)-u35k.md)
- [func entity(matching: EquipmentIdentifier) -> Entity?](tablesnapshot/entity(matching:)-vb9w.md)
- [func entity(forEquipment: some EntityEquipment) -> Entity?](tablesnapshot/entity(forequipment:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesnapshot/equipment(of:childrenof:)-4z4s1)*