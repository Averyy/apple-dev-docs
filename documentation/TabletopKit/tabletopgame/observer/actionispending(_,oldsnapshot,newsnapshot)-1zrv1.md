# actionIsPending(_:oldSnapshot:newSnapshot:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Called once for every action in the update in which it is provisionally accepted to begin contributing to the speculative visible table state, regardless of whether that action passes provisional validation. Local actions become pending in the update after they are added. Remote player actions become pending in the update in which the network request is received. The ordering of pending actions is ordered within each player, but each player in a network session may observe a different relative ordering of pending actions originating from different players. Most actions which pass initial validation create a difference in the state between `oldSnapshot` and `newSnapshot` that can be detected if needed. If the action did not pass validation on initial add to pending, the table state in `oldSnapshot` and `newSnapshot` will be identical. In a network session, the validity of an action may change one or more times between becoming pending and being confirmed or rolled back as the order of earlier actions is settled, if there are conflicts between actions. However, in practice, conflicting actions from different players should not be common.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func actionIsPending(_ action: some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/actionispending(_:oldsnapshot:newsnapshot:)-1zrv1)*