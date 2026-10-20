# actionWasCancelled(_:reason:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called once for each action which was later cancelled from the shared network table state after being confirmed due to the action of either a `jumpToBookmark` operation or due to an interaction that added it or an action it depended on being cancelled. `actionWasCancelled` callbacks are also reliably ordered with `actionWasConfirmed` and `actionWasRolledBack` callbacks.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func actionWasCancelled(_ action: some TabletopAction, reason: TabletopGame.ActionCancellationReason)
```

## Default Implementations

### TabletopGame.Observer Implementations
- [func actionWasCancelled(some TabletopAction, reason: TabletopGame.ActionCancellationReason)](./actionwascancelled%28_,reason%29-15sdh.md)
  Called once for each action which was later cancelled from the shared network table state after being confirmed due to the action of either a `jumpToBookmark` operation or due to an interaction that added it or an action it depended on being cancelled. `actionWasCancelled` callbacks are also reliably ordered with `actionWasConfirmed` and `actionWasRolledBack` callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/actionwascancelled(_:reason:))*