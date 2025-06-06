# interactionWasUpdated(_:snapshot:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

Called whenever any player interaction (local or remote) is updated. Remote player interaction updates always include phase `.started` and `.ended` or `.cancelled` but may not include a phase `.update` for every change to the pose or proposedDestination.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func interactionWasUpdated(_ value: TabletopInteraction.Value, snapshot: TableSnapshot)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/interactionwasupdated(_:snapshot:))*