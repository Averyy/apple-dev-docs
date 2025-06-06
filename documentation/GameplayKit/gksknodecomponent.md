# GKSKNodeComponent

**Framework**: GameplayKit  
**Kind**: class

A component that manages a SpriteKit node.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class GKSKNodeComponent
```

#### Overview

Adding a [`GKSKNodeComponent`](gksknodecomponent.md) object to an entity automatically updates the [`entity`](https://developer.apple.com/documentation/SpriteKit/SKNode/entity) property of the component’s SpriteKit node (an [`SKNode`](https://developer.apple.com/documentation/SpriteKit/SKNode) object) to point to that entity.

When you add entities and components to a node in the Xcode SpriteKit scene editor, Xcode automatically creates a [`GKSKNodeComponent`](gksknodecomponent.md) object to manage the relationship between that SpriteKit node and the [`GKEntity`](gkentity.md) object that node represents. Load the scene file with the [`GKScene`](gkscene.md) class to access these entities and components.

> 💡 **Tip**:  The [`GKSKNodeComponent`](gksknodecomponent.md) class adopts the [`GKAgentDelegate`](gkagentdelegate.md) protocol. If you use the [`GKAgent2D`](gkagent2d.md) class to drive the movement of game entities, set your [`GKSKNodeComponent`](gksknodecomponent.md) instance as the delegate for the entity’s agent, and GameplayKit will automatically synchronize the agent and its SpriteKit representation.

 The [`GKSKNodeComponent`](gksknodecomponent.md) class adopts the [`GKAgentDelegate`](gkagentdelegate.md) protocol. If you use the [`GKAgent2D`](gkagent2d.md) class to drive the movement of game entities, set your [`GKSKNodeComponent`](gksknodecomponent.md) instance as the delegate for the entity’s agent, and GameplayKit will automatically synchronize the agent and its SpriteKit representation.

For more information on Entity-Component architecture, read [`Entities and Components`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a SpriteKit Component
- [init(node: SKNode)](gksknodecomponent/init(node:).md)
  Initializes a component to manage the specified SpriteKit node.
### Accessing the Component’s SpriteKit Node
- [var node: SKNode](gksknodecomponent/node.md)
  The SpriteKit node managed by the component.

## Relationships

### Inherits From
- [GKComponent](gkcomponent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [GKAgentDelegate](gkagentdelegate.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class GKScene](gkscene.md)
  A container for associating GameplayKit objects with a SpriteKit scene.
- [protocol GKSceneRootNodeType](gkscenerootnodetype.md)
  Identifies scene classes from other frameworks that support embedded GameplayKit information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gksknodecomponent)*