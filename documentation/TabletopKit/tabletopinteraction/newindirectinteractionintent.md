# TabletopInteraction.NewIndirectInteractionIntent

**Framework**: TabletopKit  
**Kind**: struct

An object that represent the developer’s intent when a new indirect interaction is proposed by the system

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct NewIndirectInteractionIntent
```

## Topics

### Type Properties
- [static let reject: TabletopInteraction.NewIndirectInteractionIntent](tabletopinteraction/newindirectinteractionintent/reject.md)
  Return `reject` to indicate that interaction should not be started
### Type Methods
- [static func accept(configuration: TabletopInteraction.Configuration, constants: TabletopInteraction.IndirectInteractionConstants) -> TabletopInteraction.NewIndirectInteractionIntent](tabletopinteraction/newindirectinteractionintent/accept(configuration:constants:).md)
  Return `accept` to indicate that the interaction should be allowed to start and to specify its constants and initial configuration

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/newindirectinteractionintent)*