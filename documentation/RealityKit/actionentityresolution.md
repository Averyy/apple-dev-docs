# ActionEntityResolution

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Options available to determine the resolution method for a target entity in an action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
enum ActionEntityResolution
```

#### Overview

Use this to resolve the entity an action should target. For example, [`ImpulseAction`](./impulseaction.md) structure accepts this enumeration as an initializer argument to resolve the entity.

## Topics

### Operators
- [static func == (ActionEntityResolution, ActionEntityResolution) -> Bool](./actionentityresolution/eqeq%28_,_%29.md)
  Indicates whether two action entity resolutions are equal.
### Enumeration Cases
- [ActionEntityResolution.entityNamed(_:)](./actionentityresolution/entitynamed%28_%29.md)
  An option that resolves an entity from the specified name within the scene of the entity playing the action.
- [case entityPath(BindTarget.EntityPath)](./actionentityresolution/entitypath%28_%29.md)
  An option that resolves an entity by specifying a bind path relative to the entity playing the action.
### Initializers
- [init(from: any Decoder) throws](./actionentityresolution/init%28from%29.md)
  Creates a new instance from a decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](./actionentityresolution/encode%28to%29.md)
  Writes the action entity resolution data into an encoder.
### Type Properties
- [static var sourceEntity: ActionEntityResolution](./actionentityresolution/sourceentity.md)
  Resolves to the source entity that is playing the action.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)

## See Also

### Action management
- [protocol EntityAction](./entityaction.md)
  A protocol that defines an action for an entity.
- [struct ActionAnimation](./actionanimation.md)
  Defines an an action animation.
- [protocol ActionHandlerProtocol](./actionhandlerprotocol.md)
  The base protocol for action handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionentityresolution)*