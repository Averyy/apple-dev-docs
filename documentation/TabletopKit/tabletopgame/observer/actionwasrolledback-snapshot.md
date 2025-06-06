# actionWasRolledBack(_:snapshot:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func actionWasRolledBack(_ action: some TabletopAction, snapshot: TableSnapshot)
```

## See Also

- [func validateAction(some TabletopAction, snapshot: TableSnapshot) -> Bool](tabletopgame/observer/validateaction(_:snapshot:).md)
  Called locally for local actions Called on the leader for all actions Must be a pure function
- [func actionIsPending(some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot)](tabletopgame/observer/actionispending(_:oldsnapshot:newsnapshot:).md)
- [func actionWasConfirmed(some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot)](tabletopgame/observer/actionwasconfirmed(_:oldsnapshot:newsnapshot:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/actionwasrolledback(_:snapshot:))*