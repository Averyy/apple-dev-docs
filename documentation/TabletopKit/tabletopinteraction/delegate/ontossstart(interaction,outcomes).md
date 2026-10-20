# onTossStart(interaction:outcomes:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Implement `onTossStart(interaction:outcomes)` to be notified that the toss has just started simulating and to receive the outcome of the simulation. If the provided outcome is set to the equipment via actions, the equipment will retain the final state of the simulation even after the simulation ended.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func onTossStart(interaction: TabletopInteraction, outcomes: [TabletopInteraction.TossOutcome])
```

## Parameters

- `interaction`: The interaction corresponding to this toss.
- `outcomes`: The outcomes of all the equipment tossed.

## Default Implementations

### TabletopInteraction.Delegate Implementations
- [func onTossStart(interaction: TabletopInteraction, outcomes: [TabletopInteraction.TossOutcome])](./ontossstart%28interaction,outcomes%29-8v0lv.md)
  Implement `onTossStart(interaction:outcomes)` to be notified that the toss has just started simulating and to receive the outcome of the simulation. If the provided outcome is set to the equipment via actions, the equipment will retain the final state of the simulation even after the simulation ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/delegate/ontossstart(interaction:outcomes:))*