# TabletopInteraction.NewDirectInteractionIntent

**Framework**: TabletopKit  
**Kind**: struct

An object that represent the developer’s intent when a new direct interaction is proposed by the system

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct NewDirectInteractionIntent
```

## Topics

### Rejecting the intent
- [static let reject: TabletopInteraction.NewDirectInteractionIntent](tabletopinteraction/newdirectinteractionintent/reject.md)
  Return `reject` to indicate that interaction should not be started
### Accepting the intent
- [static func accept(configuration: TabletopInteraction.Configuration, constants: TabletopInteraction.DirectInteractionConstants) -> TabletopInteraction.NewDirectInteractionIntent](tabletopinteraction/newdirectinteractionintent/accept(configuration:constants:).md)
  Return `accept` to indicate that the interaction should be allowed to start and to specify its constants and initial configuration

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [TabletopInteraction.NewInteractionIntent](tabletopinteraction/newinteractionintent.md)
- [TabletopInteraction.NewIndirectInteractionIntent](tabletopinteraction/newindirectinteractionintent.md)
  An object that represent the developer’s intent when a new indirect interaction is proposed by the system


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/newdirectinteractionintent)*