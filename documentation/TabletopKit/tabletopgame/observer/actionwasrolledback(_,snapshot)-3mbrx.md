# actionWasRolledBack(_:snapshot:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Called once for each action which failed validation in the update in which it failed to be confirmed as a part of the shared network table state.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func actionWasRolledBack(_ action: some TabletopAction, snapshot: TableSnapshot)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/actionwasrolledback(_:snapshot:)-3mbrx)*