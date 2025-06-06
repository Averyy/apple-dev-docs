# ActionEntityResolution

**Framework**: RealityKit  
**Kind**: enum

Options available to determine the resolution method for a target entity in an action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum ActionEntityResolution
```

#### Overview

Use this to resolve the entity an action should target. For example, [`ImpulseAction`](impulseaction.md) structure accepts this enumeration as an initializer argument to resolve the entity.

## Topics

### Operators
- [static func == (ActionEntityResolution, ActionEntityResolution) -> Bool](actionentityresolution/==(_:_:).md)
  Indicates whether two action entity resolutions are equal.
### Enumeration Cases
- [ActionEntityResolution.entityNamed(_:)](actionentityresolution/entitynamed(_:).md)
  An option that resolves an entity from the specified name within the scene of the entity playing the action.
- [case entityPath(BindTarget.EntityPath)](actionentityresolution/entitypath(_:).md)
  An option that resolves an entity by specifying a bind path relative to the entity playing the action.
### Initializers
- [init(from: any Decoder) throws](actionentityresolution/init(from:).md)
  Creates a new instance from a decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](actionentityresolution/encode(to:).md)
  Writes the action entity resolution data into an encoder.
### Type Properties
- [static var sourceEntity: ActionEntityResolution](actionentityresolution/sourceentity.md)
  Resolves to the source entity that is playing the action.
### Default Implementations
- [Equatable Implementations](actionentityresolution/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [protocol EntityAction](entityaction.md)
  A protocol that defines an action for an entity.
- [struct ActionAnimation](actionanimation.md)
  Defines an an action animation.
- [protocol ActionHandlerProtocol](actionhandlerprotocol.md)
  The base protocol for action handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionentityresolution)*