# Equipment

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for equipment that players directly interact with in a game.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol Equipment : Identifiable where Self.ID == EquipmentIdentifier
```

#### Overview

To represent equipment in your game, such as cards, pieces, and dice, following these steps:

- Create a structure that conforms to this protocol.
- Declare the [`initialState`](equipment/initialstate.md) property as either [`BaseEquipmentState`](baseequipmentstate.md), [`DieState`](diestate.md), or [`CardState`](cardstate.md), depending on the type of data you want TabletopKit to sync between players. For more complex data, use [`RawValueState`](rawvaluestate.md).
- Declare the `id` property as a [`EquipmentIdentifier`](equipmentidentifier.md) structure.
- Implement an initializer that sets the `id` and [`initialState`](equipment/initialstate.md) properties.

Optionally, implement the [`layoutChildren(for:visualState:)`](equipment/layoutchildren(for:visualstate:).md) method for equipment that represents groups, and the [`restingOrientation(state:)`](equipment/restingorientation(state:).md) method to provide a custom resting orientation.

## Topics

### Gettting the initial state of the equipment
- [var initialState: Self.State](equipment/initialstate.md)
- [associatedtype State : EquipmentState](equipment/state.md)
### Displaying the equipment
- [func layoutChildren(for: TableSnapshot, visualState: TableVisualState) -> any EquipmentLayout](equipment/layoutchildren(for:visualstate:).md)
  This function provides the layout of the direct children of this equipment and is called whenever the snapshot changes. Override it to provide a custom layout. The output of this function is considered to be only a function of its inputs. Reaching out to data outside what is provided might result in undefined behavior.
- [func restingOrientation(state: Self.State) -> Rotation3D](equipment/restingorientation(state:).md)
  The resting orientation of the equipment given the current State.

## Relationships

### Inherits From
- [Identifiable](../Swift/Identifiable.md)
### Inherited By
- [EntityEquipment](entityequipment.md)

## See Also

- [protocol EntityEquipment](entityequipment.md)
  A protocol for equipment in a game that you render using RealityKit.
- [struct EquipmentIdentifier](equipmentidentifier.md)
  A unique identifier for equipment.
- [protocol EquipmentState](equipmentstate.md)
  A protocol for the equipment data that TabletopKit syncs between players.
- [struct BaseEquipmentState](baseequipmentstate.md)
  A state for equipment that contains no equipment-specific data.
- [struct CardState](cardstate.md)
  A state for cards that contains face up and down information.
- [struct DieState](diestate.md)
  A state for dice that contains the current value.
- [struct RawValueState](rawvaluestate.md)
  A state for equipment that contains a game-specific value.
- [enum ControllingSeats](controllingseats.md)
  The seats that can manipulate or interact with the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipment)*