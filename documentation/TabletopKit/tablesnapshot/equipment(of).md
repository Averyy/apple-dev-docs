# equipment(of:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func equipment<E>(of type: E.Type) -> [(E, E.State)] where E : Equipment
```

## See Also

### Getting information on equipment
- [func equipment<E>(of: E.Type, childrenOf: some Equipment) -> [(E, E.State)]](./equipment%28of,childrenof%29-4z4s1.md)
- [func equipment<E>(of: E.Type, childrenOf: EquipmentIdentifier) -> [(E, E.State)]](./equipment%28of,childrenof%29-5w137.md)
- [func equipment<E>(of: E.Type, matching: some Sequence<EquipmentIdentifier>) -> [(E, E.State)]](./equipment%28of,matching%29-7ai0c.md)
- [func equipment<E>(of: E.Type, matching: EquipmentIdentifier) -> (E, E.State)?](./equipment%28of,matching%29-8qve2.md)
- [func equipmentIDs() -> [EquipmentIdentifier]](./equipmentids%28%29.md)
- [func equipmentIDs(childrenOf: some Equipment) -> [EquipmentIdentifier]](./equipmentids%28childrenof%29-432sk.md)
- [func equipmentIDs(childrenOf: EquipmentIdentifier) -> [EquipmentIdentifier]](./equipmentids%28childrenof%29-f1sp.md)
- [func state(matching: EquipmentIdentifier) -> (any EquipmentState)?](./state%28matching%29-u35k.md)
- [func entity(matching: EquipmentIdentifier) -> Entity?](./entity%28matching%29-vb9w.md)
- [func entity(forEquipment: some EntityEquipment) -> Entity?](./entity%28forequipment%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesnapshot/equipment(of:))*