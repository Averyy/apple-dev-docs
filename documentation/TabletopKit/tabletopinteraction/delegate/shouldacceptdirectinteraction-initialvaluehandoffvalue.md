# shouldAcceptDirectInteraction(initialValue:handoffValue:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

Implement `shouldAcceptDirectInteraction(initialValue:handoffValue)` to provide the constants and initial configuration for the new direct interaction, and to decide if the new interaction should be accepted or rejected. If the function is not implemented, the default implementation will be used, which will call into the more generic `shouldAcceptInteraction(initialValue:handoffValue)`.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func shouldAcceptDirectInteraction(initialValue: TabletopInteraction.Value, handoffValue: TabletopInteraction.Value?) -> TabletopInteraction.NewDirectInteractionIntent
```

#### Return Value

The intent that describes the action to be taken on this new interaction (reject or accept with constants and configuration)

## Parameters

- `initialValue`: The initial   for this interaction, using the default configuration and constants.
- `handoffValue`: If not  , this interaction is trying to take control of an equipment already controlled by another interaction,   causing a “handoff” of the equipment. The value provides the most recent data of the interaction that is   currently controlling the equipment.

## See Also

- [func shouldAcceptIndirectInteraction(initialValue: TabletopInteraction.Value, handoffValue: TabletopInteraction.Value?) -> TabletopInteraction.NewIndirectInteractionIntent](tabletopinteraction/delegate/shouldacceptindirectinteraction(initialvalue:handoffvalue:).md)
  Implement `shouldAcceptIndirectInteraction(initialValue:handoffValue)` to provide the constants and initial configuration for the new indirect interaction, and to decide if the new interaction should be accepted or rejected. If the function is not implemented, the default implementation will be used, which will call into the more generic `shouldAcceptInteraction(initialValue:handoffValue)`.
- [func shouldAcceptInteraction(initialValue: TabletopInteraction.Value, handoffValue: TabletopInteraction.Value?) -> TabletopInteraction.NewInteractionIntent](tabletopinteraction/delegate/shouldacceptinteraction(initialvalue:handoffvalue:).md)
  Implement `shouldAcceptInteraction(initialValue:handoffValue)` to provide the initial configuration for new interactions, and to decide if a new interaction should be accepted or rejected. If this function is not implemented, the default implementation will be used which will reject all handoff interactions and will accept all other interactions providing the default configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/delegate/shouldacceptdirectinteraction(initialvalue:handoffvalue:))*