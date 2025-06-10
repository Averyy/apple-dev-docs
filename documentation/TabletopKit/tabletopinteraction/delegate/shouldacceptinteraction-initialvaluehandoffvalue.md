# shouldAcceptInteraction(initialValue:handoffValue:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

Implement `shouldAcceptInteraction(initialValue:handoffValue)` to provide the initial configuration for new interactions, and to decide if a new interaction should be accepted or rejected. If this function is not implemented, the default implementation will be used which will reject all handoff interactions and will accept all other interactions providing the default configuration.

**Availability**:
- visionOS 2.2+

## Declaration

```swift
func shouldAcceptInteraction(initialValue: TabletopInteraction.Value, handoffValue: TabletopInteraction.Value?) -> TabletopInteraction.NewInteractionIntent
```

#### Return Value

The intent that describes the action to be taken on this new interaction (reject or accept with configuration)

## Parameters

- `initialValue`: The initial   for this interaction, calculated using the default configuration and constants.
- `handoffValue`: If not  , this interaction is trying to take control of an equipment already controlled by another interaction,   causing a “handoff” of the equipment. The value provides the most recent data of the interaction that is   currently controlling the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/delegate/shouldacceptinteraction(initialvalue:handoffvalue:))*