# TabletopInteraction.NewDirectInteractionIntent

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

An object that represent the developer’s intent when a new direct interaction is proposed by the system

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct NewDirectInteractionIntent
```

## Topics

### Rejecting the intent
- [static let reject: TabletopInteraction.NewDirectInteractionIntent](./newdirectinteractionintent/reject.md)
  Return `reject` to indicate that interaction should not be started
### Accepting the intent
- [static func accept(configuration: TabletopInteraction.Configuration, constants: TabletopInteraction.DirectInteractionConstants) -> TabletopInteraction.NewDirectInteractionIntent](./newdirectinteractionintent/accept%28configuration,constants%29.md)
  Return `accept` to indicate that the interaction should be allowed to start and to specify its constants and initial configuration

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling interaction intents
- [TabletopInteraction.NewInteractionIntent](./newinteractionintent.md)
- [TabletopInteraction.NewIndirectInteractionIntent](./newindirectinteractionintent.md)
  An object that represent the developer’s intent when a new indirect interaction is proposed by the system


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/newdirectinteractionintent)*