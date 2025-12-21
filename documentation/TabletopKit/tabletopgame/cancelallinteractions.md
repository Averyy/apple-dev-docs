# cancelAllInteractions()

**Framework**: TabletopKit  
**Kind**: method

Cancels all local and remote interactions. This releases control of all the equipment and rolls back all the actions added to the canceled interaction.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func cancelAllInteractions()
```

## See Also

- [func cancelInteraction(matching: TabletopInteraction.Identifier)](tabletopgame/cancelinteraction(matching:).md)
  Cancel the local or remote interaction matching the given identifier. This causes any actions added to it to be rolled back, and releases the controlled equipment and any tossed equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/cancelallinteractions())*