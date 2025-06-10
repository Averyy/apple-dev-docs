# TabletopKit

**Framework**: TabletopKit  
**Kind**: module

Create multiplayer spatial games on a virtual table surface and use FaceTime to invite players.

**Availability**:
- visionOS 2.0+

#### Overview

TabletopKit helps you create a spatial multiplayer game on a table surface for visionOS, where players join your game using SharePlay. TabletopKit provides support for designing your game, implementing rules, rendering effects, and syncing multiplayer game state.

![A representation of a tabletop game in spatial mode in visionOS.](https://docs-assets.developer.apple.com/published/57db470ae11aa75bdce3aba0477c2520/tabletopkit-framework-hero%402x.png)

Follow these steps to implement your TabletopKit game:

- Configure your game on the tabletop and create the game pieces or equipment that players interact with. You provide the renderer that draws your game and its pieces.
- Implement the game rules and player interactions with the equipment. TabletopKit processes and represents player gestures as interactions. You observe the interactions and append your game-specific actions.
- Add effects to the RealityKit entities of renderable equipment and trigger them during interactions. For example, play a sound effect when a player throws a piece or an animation when a player achieves a goal.
- Set up multiplayer using SharePlay. Start a Group Activities session and provide it to TabletopKit. Then customize the spatial experience of your game. For example,  place the players in their seats and spectators around the room.

To get started, create a [`TabletopGame`](tabletopgame.md) object that represents your game instance and a [`TableSetup`](tablesetup.md) object that represents your game layout and equipment.

## Topics

### Essentials
- [Creating tabletop games](tabletopkitsample.md)
  Develop a spatial board game where multiple players interact with pieces on a table.
- [Synchronizing group gameplay with TabletopKit](synchronizing-group-gameplay-with-tabletopkit.md)
  Maintain game state across multiple players in a race to capture all the coins.
- [class TabletopGame](tabletopgame.md)
  An object that manages the setup and gameplay of a tabletop game.
- [struct TableSetup](tablesetup.md)
  An object that represents the arrangement of seats, equipment, and counters around the game table.
- [protocol Tabletop](tabletop.md)
  A protocol for the table surface in your game.
- [protocol EntityTabletop](entitytabletop.md)
  A protocol for the table surface in your game when you render it using RealityKit.
- [struct TabletopShape](tabletopshape.md)
  An object that represents the physical properties of the table.
### Seats
- [protocol TableSeat](tableseat.md)
  A protocol for seats at the table that players occupy.
- [protocol EntityTableSeat](entitytableseat.md)
  A protocol for seats at the table that you render using RealityKit.
- [struct TableSeatIdentifier](tableseatidentifier.md)
  A unique identifier for seats.
- [struct TableSeatState](tableseatstate.md)
  The data associated with a seat that a player occupies.
- [protocol SeatState](seatstate.md)
  A protocol for seat data that TabletopKit syncs between players.
### Equipment
- [protocol Equipment](equipment.md)
  A protocol for equipment that players directly interact with in a game.
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
### Equipment layout
- [protocol EquipmentLayout](equipmentlayout.md)
  A protocol for objects that describe the layout of equipment.
- [struct DefaultEquipmentLayout](defaultequipmentlayout.md)
  An object that provides a standard configuration for equipment layout.
- [struct EquipmentPose2D](equipmentpose2d.md)
  An object that represents the position and rotation of equipment on the XZ plane.
- [struct EquipmentPose3D](equipmentpose3d.md)
  An object that represents the 3D position and orientation of equipment on the table.
### Score counters
- [struct ScoreCounter](scorecounter.md)
  An object that keeps a score in a tabletop game.
### Players
- [struct Player](player.md)
  A player in a tabletop game.
- [struct PlayerIdentifier](playeridentifier.md)
  A unique identifier for players.
### Actions
- [protocol TabletopAction](tabletopaction.md)
  A protocol for objects that describe an action in a tabletop game.
- [struct MoveEquipmentAction](moveequipmentaction.md)
  An action that moves a piece of equipment on the table or changes the grouping.
- [struct UpdateEquipmentAction](updateequipmentaction.md)
  An action that updates properties of equipment on the table.
- [struct SetTurnAction](setturnaction.md)
  An action that sets the current seats participating in the current turn.
- [struct UpdateCounterAction](updatecounteraction.md)
  An action that updates the game counter.
- [struct CreateBookmarkAction](createbookmarkaction.md)
  An action that takes a snapshot of the game.
### Interactions
- [class TabletopInteraction](tabletopinteraction.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [struct TossableRepresentation](tossablerepresentation.md)
  An object that represents geometric shapes that the player can throw during gameplay, such as dice.
- [struct TableSnapshot](tablesnapshot.md)
  A snapshot of the current state of the table.
- [struct TableVisualState](tablevisualstate.md)
  A structure that represents the appearance of an object on the table.
- [struct TableCursor](tablecursor.md)
  A cursor conveys information about one equipment that is currently being controlled by an interaction.
- [struct TableCursorIdentifier](tablecursoridentifier.md)
  A unique identifier for cursors.
### Bookmarks
- [struct StateBookmark](statebookmark.md)
  A snapshot of the game state at a point in time.
- [struct StateBookmarkIdentifier](statebookmarkidentifier.md)
  A unique identifier for bookmarks.
### Multiplayer network session
- [class TabletopNetworkSession](tabletopnetworksession.md)
  An object that coordinates network-related tasks in multiplayer games.
- [protocol TabletopNetworkSessionCoordinator](tabletopnetworksessioncoordinator.md)
  A protocol for objects that manage network sessions between peers.
- [enum TabletopSendMessageResult](tabletopsendmessageresult.md)
  The possible results of sending messages in a network session.
### Debugging
- [struct DebugDrawOptions](debugdrawoptions.md)
  Types of items in a rendering that you want to debug.
### Protocols
- [protocol CustomAction](customaction.md)
  A protocol that represents an action whose behavior is implemented outside of TabletopKit. A custom action that can be applied to a `TableState`.
- [protocol CustomEquipmentState](customequipmentstate.md)
  A specialized protocol for the equipment state that allows to accommodate custom data that TabletopKit syncs between players.
- [protocol MutableEquipmentState](mutableequipmentstate.md)
  A protocol for equipment data that TabletopKit syncs between players, and that can be mutated.
### Structures
- [struct CounterCollection](countercollection.md)
  A collection of score counters that can be inspected and modified.
- [struct EquipmentCollection](equipmentcollection.md)
  A collection of equipment whose state can be inspected and modified.
- [struct EquipmentStateCollection](equipmentstatecollection.md)
  A collection of equipment states that can be inspected and modified.
- [struct TableState](tablestate.md)
  The state of the table that can be queried and modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TabletopKit)*