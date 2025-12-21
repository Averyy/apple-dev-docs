# add(equipment:)

**Framework**: TabletopKit  
**Kind**: method

Add the given equipment to the table setup.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
mutating func add<E>(equipment: E) where E : Equipment, E.State : BitwiseCopyable, E.State : CustomEquipmentState
```

## Parameters

- `equipment`: The equipment to add.

## See Also

- [func add(equipment: some Equipment)](tablesetup/add(equipment:)-29pef.md)
  Add the given equipment to the table setup.
- [func add<E>(equipment: E)](tablesetup/add(equipment:)-294gb.md)
- [func add(equipment: some EntityEquipment)](tablesetup/add(equipment:)-24tv6.md)
- [func add(equipment: some Sequence)](tablesetup/add(equipment:)-4k6m6.md)
  Add the given equipment to the table setup.
- [func add<E>(equipment: some Sequence)](tablesetup/add(equipment:)-3d7h9.md)
- [func add(equipment: some Sequence)](tablesetup/add(equipment:)-9syh2.md)
- [func add<E>(equipment: some Sequence)](tablesetup/add(equipment:)-9h887.md)
  Add the given equipment to the table setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesetup/add(equipment:)-7qwj2)*