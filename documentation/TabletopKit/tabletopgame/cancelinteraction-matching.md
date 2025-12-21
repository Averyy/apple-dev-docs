# cancelInteraction(matching:)

**Framework**: TabletopKit  
**Kind**: method

Cancel the local or remote interaction matching the given identifier. This causes any actions added to it to be rolled back, and releases the controlled equipment and any tossed equipment.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func cancelInteraction(matching interactionID: TabletopInteraction.Identifier)
```

## See Also

- [func cancelAllInteractions()](tabletopgame/cancelallinteractions.md)
  Cancels all local and remote interactions. This releases control of all the equipment and rolls back all the actions added to the canceled interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/cancelinteraction(matching:))*