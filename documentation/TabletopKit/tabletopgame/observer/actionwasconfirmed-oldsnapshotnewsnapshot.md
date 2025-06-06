# actionWasConfirmed(_:oldSnapshot:newSnapshot:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func actionWasConfirmed(_ action: some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot)
```

## See Also

- [func validateAction(some TabletopAction, snapshot: TableSnapshot) -> Bool](tabletopgame/observer/validateaction(_:snapshot:).md)
  Called locally for local actions Called on the leader for all actions Must be a pure function
- [func actionIsPending(some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot)](tabletopgame/observer/actionispending(_:oldsnapshot:newsnapshot:).md)
- [func actionWasRolledBack(some TabletopAction, snapshot: TableSnapshot)](tabletopgame/observer/actionwasrolledback(_:snapshot:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/actionwasconfirmed(_:oldsnapshot:newsnapshot:))*