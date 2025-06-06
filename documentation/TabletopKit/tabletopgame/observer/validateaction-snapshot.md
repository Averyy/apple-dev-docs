# validateAction(_:snapshot:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

Called locally for local actions Called on the leader for all actions Must be a pure function

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func validateAction(_ action: some TabletopAction, snapshot: TableSnapshot) -> Bool
```

## See Also

- [func actionIsPending(some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot)](tabletopgame/observer/actionispending(_:oldsnapshot:newsnapshot:).md)
- [func actionWasConfirmed(some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot)](tabletopgame/observer/actionwasconfirmed(_:oldsnapshot:newsnapshot:).md)
- [func actionWasRolledBack(some TabletopAction, snapshot: TableSnapshot)](tabletopgame/observer/actionwasrolledback(_:snapshot:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/validateaction(_:snapshot:))*