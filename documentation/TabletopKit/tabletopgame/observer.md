# TabletopGame.Observer

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for objects that progress gameplay when players take actions.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol Observer : AnyObject
```

## Topics

### Handling interaction updates
- [func interactionWasUpdated(TabletopInteraction.Value, snapshot: TableSnapshot)](tabletopgame/observer/interactionwasupdated(_:snapshot:).md)
  Called whenever any player interaction (local or remote) is updated. Remote player interaction updates always include phase `.started` and `.ended` or `.cancelled` but may not include a phase `.update` for every change to the pose or proposedDestination.
### Validating actions
- [func validateAction(some TabletopAction, snapshot: TableSnapshot) -> Bool](tabletopgame/observer/validateaction(_:snapshot:).md)
  Called locally for local actions Called on the leader for all actions Must be a pure function
- [func actionIsPending(some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot)](tabletopgame/observer/actionispending(_:oldsnapshot:newsnapshot:).md)
- [func actionWasConfirmed(some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot)](tabletopgame/observer/actionwasconfirmed(_:oldsnapshot:newsnapshot:).md)
- [func actionWasRolledBack(some TabletopAction, snapshot: TableSnapshot)](tabletopgame/observer/actionwasrolledback(_:snapshot:).md)
### Handling seat actions
- [func playerChangedSeats(Player, oldSeat: (any TableSeat)?, newSeat: (any TableSeat)?, snapshot: TableSnapshot)](tabletopgame/observer/playerchangedseats(_:oldseat:newseat:snapshot:).md)
  Called every time the Seat for any player has changed
- [func stateDidResetToBookmark(StateBookmarkIdentifier)](tabletopgame/observer/statedidresettobookmark(_:).md)
### Handling cancellations
- [func actionWasCancelled(some TabletopAction, reason: TabletopGame.ActionCancellationReason)](tabletopgame/observer/actionwascancelled(_:reason:).md)

## See Also

- [func addObserver(some TabletopGame.Observer)](tabletopgame/addobserver(_:).md)
- [func removeObserver(some TabletopGame.Observer)](tabletopgame/removeobserver(_:).md)
- [TabletopGame.ActionCancellationReason](tabletopgame/actioncancellationreason.md)
  The possible reasons for cancelling an action or an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer)*