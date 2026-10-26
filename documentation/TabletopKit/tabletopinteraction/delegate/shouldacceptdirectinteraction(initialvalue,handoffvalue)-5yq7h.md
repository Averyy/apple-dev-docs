# shouldAcceptDirectInteraction(initialValue:handoffValue:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

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

- `initialValue`: The initial `Value` for this interaction, using the default configuration and constants.
- `handoffValue`: If not `nil`, this interaction is trying to take control of an equipment already controlled by another interaction, causing a “handoff” of the equipment. The value provides the most recent data of the interaction that is currently controlling the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/delegate/shouldacceptdirectinteraction(initialvalue:handoffvalue:)-5yq7h)*