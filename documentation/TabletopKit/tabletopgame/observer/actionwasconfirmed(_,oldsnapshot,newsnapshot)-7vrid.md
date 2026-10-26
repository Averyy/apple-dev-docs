# actionWasConfirmed(_:oldSnapshot:newSnapshot:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Called once for each action which passed validation in the update in which it is confirmed as a part of the shared network table state. All players in a network session are guaranteed to observe the same sequence of `actionWasConfirmed` and `actionWasRolledBack` callbacks. In a network session, these callbacks are delayed behind `actionIsPending` callbacks by approximately a network round trip time.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func actionWasConfirmed(_ action: some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/actionwasconfirmed(_:oldsnapshot:newsnapshot:)-7vrid)*