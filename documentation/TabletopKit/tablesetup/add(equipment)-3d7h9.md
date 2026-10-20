# add(equipment:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- visionOS 26.0+

## Declaration

```swift
mutating func add<E>(equipment: some Sequence) where E : EntityEquipment, E.State : BitwiseCopyable, E.State : CustomEquipmentState
```

## See Also

### Adding equipment for gameplay
- [func add(equipment: some Equipment)](./add%28equipment%29-29pef.md)
  Add the given equipment to the table setup.
- [func add<E>(equipment: E)](./add%28equipment%29-294gb.md)
- [func add(equipment: some EntityEquipment)](./add%28equipment%29-24tv6.md)
- [func add<E>(equipment: E)](./add%28equipment%29-7qwj2.md)
  Add the given equipment to the table setup.
- [func add(equipment: some Sequence)](./add%28equipment%29-4k6m6.md)
  Add the given equipment to the table setup.
- [func add(equipment: some Sequence)](./add%28equipment%29-9syh2.md)
- [func add<E>(equipment: some Sequence)](./add%28equipment%29-9h887.md)
  Add the given equipment to the table setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesetup/add(equipment:)-3d7h9)*