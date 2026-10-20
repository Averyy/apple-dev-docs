# GKSKNodeComponent

**Framework**: GameplayKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface GKSKNodeComponent : GKComponent
```

#### Overview

Adding a [`GKSKNodeComponent`](./gksknodecomponent.md) object to an entity automatically updates the [`entity`](../SpriteKit/sknode/entity.md) property of the component’s SpriteKit node (an [`SKNode`](../SpriteKit/sknode.md) object) to point to that entity.

When you add entities and components to a node in the Xcode SpriteKit scene editor, Xcode automatically creates a [`GKSKNodeComponent`](./gksknodecomponent.md) object to manage the relationship between that SpriteKit node and the [`GKEntity`](./gkentity.md) object that node represents. Load the scene file with the [`GKScene`](./gkscene.md) class to access these entities and components.

> 💡 **Tip**:  The [`GKSKNodeComponent`](./gksknodecomponent.md) class adopts the [`GKAgentDelegate`](./gkagentdelegate.md) protocol. If you use the [`GKAgent2D`](./gkagent2d.md) class to drive the movement of game entities, set your [`GKSKNodeComponent`](./gksknodecomponent.md) instance as the delegate for the entity’s agent, and GameplayKit will automatically synchronize the agent and its SpriteKit representation.

For more information on Entity-Component architecture, read [Entities and Components](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a SpriteKit Component
- [init(node: SKNode)](./gksknodecomponent/init%28node%29.md)
  Initializes a component to manage the specified SpriteKit node.
### Accessing the Component’s SpriteKit Node
- [var node: SKNode](./gksknodecomponent/node.md)
  The SpriteKit node managed by the component.

## Relationships

### Inherits From
- [GKComponent](./gkcomponent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [GKAgentDelegate](./gkagentdelegate.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Xcode and SpriteKit Integration
- [class GKScene](./gkscene.md)
  A container for associating GameplayKit objects with a SpriteKit scene.
- [protocol GKSceneRootNodeType](./gkscenerootnodetype.md)
  Identifies scene classes from other frameworks that support embedded GameplayKit information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gksknodecomponent)*