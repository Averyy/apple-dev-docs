# actionWasCancelled(_:reason:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

Called once for each action which was later cancelled from the shared network table state after being confirmed due to the action of either a `jumpToBookmark` operation or due to an interaction that added it or an action it depended on being cancelled. `actionWasCancelled` callbacks are also reliably ordered with `actionWasConfirmed` and `actionWasRolledBack` callbacks.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func actionWasCancelled(_ action: some TabletopAction, reason: TabletopGame.ActionCancellationReason)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/actionwascancelled(_:reason:))*