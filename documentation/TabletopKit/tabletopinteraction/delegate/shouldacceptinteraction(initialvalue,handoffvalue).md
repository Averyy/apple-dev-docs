# shouldAcceptInteraction(initialValue:handoffValue:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method  
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

- `initialValue`: The initial `Value` for this interaction, calculated using the default configuration and constants.
- `handoffValue`: If not `nil`, this interaction is trying to take control of an equipment already controlled by another interaction, causing a “handoff” of the equipment. The value provides the most recent data of the interaction that is currently controlling the equipment.

## Default Implementations

### TabletopInteraction.Delegate Implementations
- [func shouldAcceptInteraction(initialValue: TabletopInteraction.Value, handoffValue: TabletopInteraction.Value?) -> TabletopInteraction.NewInteractionIntent](./shouldacceptinteraction%28initialvalue,handoffvalue%29-7dm2w.md)
  Implement `shouldAcceptInteraction(initialValue:handoffValue)` to provide the initial configuration for new interactions, and to decide if a new interaction should be accepted or rejected. If this function is not implemented, the default implementation will be used which will reject all handoff interactions and will accept all other interactions providing the default configuration.

## See Also

### Accepting interactions
- [func shouldAcceptDirectInteraction(initialValue: TabletopInteraction.Value, handoffValue: TabletopInteraction.Value?) -> TabletopInteraction.NewDirectInteractionIntent](./shouldacceptdirectinteraction%28initialvalue,handoffvalue%29.md)
  Implement `shouldAcceptDirectInteraction(initialValue:handoffValue)` to provide the constants and initial configuration for the new direct interaction, and to decide if the new interaction should be accepted or rejected. If the function is not implemented, the default implementation will be used, which will call into the more generic `shouldAcceptInteraction(initialValue:handoffValue)`.
- [func shouldAcceptIndirectInteraction(initialValue: TabletopInteraction.Value, handoffValue: TabletopInteraction.Value?) -> TabletopInteraction.NewIndirectInteractionIntent](./shouldacceptindirectinteraction%28initialvalue,handoffvalue%29.md)
  Implement `shouldAcceptIndirectInteraction(initialValue:handoffValue)` to provide the constants and initial configuration for the new indirect interaction, and to decide if the new interaction should be accepted or rejected. If the function is not implemented, the default implementation will be used, which will call into the more generic `shouldAcceptInteraction(initialValue:handoffValue)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/delegate/shouldacceptinteraction(initialvalue:handoffvalue:))*