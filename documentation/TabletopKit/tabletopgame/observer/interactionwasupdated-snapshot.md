# interactionWasUpdated(_:snapshot:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

Called whenever any interaction (local or remote) is updated. For local interactions, each `interactionWasUpdated` callback occurs immediately before the `TabletopInteraction.Delegate.update()` callback with the same `TabletopInteraction.Value` and the same snapshot as is accessed by `game.withCurrentSnapshot`. For remote interactions, `interactionWasUpdated` callbacks are only guaranteed to occur when the `phase` or `controlledEquipment` are updated and the `TabletopInteraction.Value` indicates only the limited information available about remote interactions viewed over the network.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func interactionWasUpdated(_ value: TabletopInteraction.Value, snapshot: TableSnapshot)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/interactionwasupdated(_:snapshot:))*