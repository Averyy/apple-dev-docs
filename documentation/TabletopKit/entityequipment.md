# EntityEquipment

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for equipment in a game that you render using RealityKit.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol EntityEquipment : Equipment
```

#### Overview

To render equipment using an entity, follow these steps:

1. Create a structure that conforms to this protocol.
2. Depending on the type of equipment, set the [`State`](equipment/state.md) type alias to either [`BaseEquipmentState`](baseequipmentstate.md), [`DieState`](diestate.md), or [`CardState`](cardstate.md).
3. Declare the `id` property as a [`EquipmentIdentifier`](equipmentidentifier.md) structure.
4. Declare the [`initialState`](equipment/initialstate.md) property as a [`State`](equipment/state.md) structure.
5. Implement an initializer that sets these properties and the [`entity`](entityequipment/entity.md) property.

```swift
struct Piece: EntityEquipment {
    typealias State = BaseEquipmentState

    var id: EquipmentIdentifier
    var entity: Entity
    var initialState: State

    @MainActor
    init(index: Int = 0, position: TableVisualState.Point2D) {
        id = .piece(index)
        entity = try! ModelEntity.load(named: "chess/queen", in: contentBundle)
        initialState = State(parentID: .table, pose: .init(position: position, rotation: .init()), entity: entity)
    }
}
```

Optionally, implement the [`layoutChildren(for:visualState:)`](equipment/layoutchildren(for:visualstate:).md) method for equipment that represents groups, and the [`restingOrientation(state:)`](equipment/restingorientation(state:).md) method to provide a custom resting position. For example, implement the [`restingOrientation(state:)`](equipment/restingorientation(state:).md) method to flip a card face down in a card game:

```swift
func restingOrientation(state: State) -> Rotation3D {
    state.faceUp ? .identity : .init(angle: .init(degrees: +180), axis: .init(x: 0, y: 0, z: 1))
}
```

## Topics

### Displaying the equipment
- [var entity: Entity](entityequipment/entity.md)
  The entity associated with the equipment.

## Relationships

### Inherits From
- [Equipment](equipment.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [Implementing playing card overlap and physical characteristics](implementing-playing-card-overlap-and-physical-characteristics.md)
  Add interactive card game behavior for a pile of playing cards with physically realistic stacking and overlapping.
- [protocol Equipment](equipment.md)
  A protocol for equipment that players directly interact with in a game.
- [struct EquipmentCollection](equipmentcollection.md)
  A collection of equipment whose state can be inspected and modified.
- [struct EquipmentIdentifier](equipmentidentifier.md)
  A unique identifier for equipment.
- [protocol EquipmentState](equipmentstate.md)
  A protocol for the equipment data that TabletopKit syncs between players.
- [struct EquipmentStateCollection](equipmentstatecollection.md)
  A collection of equipment states that can be inspected and modified.
- [struct BaseEquipmentState](baseequipmentstate.md)
  A state for equipment that contains no equipment-specific data.
- [protocol CustomEquipmentState](customequipmentstate.md)
  A specialized protocol for the equipment state that allows to accommodate custom data that TabletopKit syncs between players.
- [protocol MutableEquipmentState](mutableequipmentstate.md)
  A protocol for equipment data that TabletopKit syncs between players, and that can be mutated.
- [struct CardState](cardstate.md)
  A state for cards that contains face up and down information.
- [struct DieState](diestate.md)
  A state for dice that contains the current value.
- [struct RawValueState](rawvaluestate.md)
  A state for equipment that contains a game-specific value.
- [enum ControllingSeats](controllingseats.md)
  The seats that can manipulate or interact with the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/entityequipment)*