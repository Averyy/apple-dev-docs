# actionIsPending(_:oldSnapshot:newSnapshot:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

Called once for every action in the update in which it is provisionally accepted to begin contributing to the speculative visible table state, regardless of whether that action passes provisional validation. Local actions become pending in the update after they are added. Remote player actions become pending in the update in which the network request is received. The ordering of pending actions is ordered within each player, but each player in a network session may observe a different relative ordering of pending actions originating from different players. Most actions which pass initial validation create a difference in the state between `oldSnapshot` and `newSnapshot` that can be detected if needed. If the action did not pass validation on initial add to pending, the table state in `oldSnapshot` and `newSnapshot` will be identical. In a network session, the validity of an action may change one or more times between becoming pending and being confirmed or rolled back as the order of earlier actions is settled, if there are conflicts between actions. However, in practice, conflicting actions from different players should not be common.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func actionIsPending(_ action: some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot)
```

## See Also

- [func validateAction(some TabletopAction, snapshot: TableSnapshot) -> Bool](tabletopgame/observer/validateaction(_:snapshot:).md)
  Called to determine whether an action should be included as part of the table state based only on the action and the table state snapshot it is being applied to. Must be a pure function. Called for all actions multiple times between becoming pending and being confirmed (or rolled back) as necessary to determine an internally consistent speculative visible table state each update, and, finally, to resolve the internally consistent network shared table state. Potentially also called after confirmed if an interaction that added actions is cancelled to determine a new internally consistent shared network table state.
- [func actionWasConfirmed(some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot)](tabletopgame/observer/actionwasconfirmed(_:oldsnapshot:newsnapshot:).md)
  Called once for each action which passed validation in the update in which it is confirmed as a part of the shared network table state. All players in a network session are guaranteed to observe the same sequence of `actionWasConfirmed` and `actionWasRolledBack` callbacks. In a network session, these callbacks are delayed behind `actionIsPending` callbacks by approximately a network round trip time.
- [func actionWasRolledBack(some TabletopAction, snapshot: TableSnapshot)](tabletopgame/observer/actionwasrolledback(_:snapshot:).md)
  Called once for each action which failed validation in the update in which it failed to be confirmed as a part of the shared network table state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/actionispending(_:oldsnapshot:newsnapshot:))*