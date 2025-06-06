# GKComponent

**Framework**: GameplayKit  
**Kind**: class

The abstract superclass for creating objects that add specific gameplay functionality to an entity.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKComponent
```

#### Overview

[`GKComponent`](gkcomponent.md) is the abstract superclass for custom component classes you create when building a game with Entity-Component architecture. In this architecture, an  is an object relevant to the game, and a  is an object that handles specific aspects of an entity’s behavior in a general way. Because a component’s scope of functionality is limited, you can reuse the same component class for many different kinds of entities.

You create components by subclassing [`GKComponent`](gkcomponent.md) to implement reusable behavior. Then, you build game entities by creating [`GKEntity`](gkentity.md) objects and using the [`addComponent(_:)`](gkentity/addcomponent(_:).md) method to attach instances of your custom component classes.

At runtime, a component-based game needs to dispatch periodic logic—from an update/render loop method such as [`update(_:)`](https://developer.apple.com/documentation/SpriteKit/SKScene/update(_:)) (SpriteKit) or [`renderer(_:updateAtTime:)`](https://developer.apple.com/documentation/SceneKit/SCNSceneRendererDelegate/renderer(_:updateAtTime:)) (SceneKit), or a [`CADisplayLink`](https://developer.apple.com/documentation/QuartzCore/CADisplayLink) (iOS) or [`CVDisplayLink`](https://developer.apple.com/documentation/CoreVideo/CVDisplayLink) (macOS) timer in a custom rendering engine—to each of its components. GameplayKit provides two mechanisms for dispatching updates:

- Per-entity. Call each entity’s [`update(deltaTime:)`](gkentity/update(deltatime:).md) method, which will then forward to the [`update(deltaTime:)`](gkcomponent/update(deltatime:).md) method of each component. This option can be quickly implemented in games with a small number of entities and components.
- Per-component. Use a [`GKComponentSystem`](gkcomponentsystem.md) object to handle all instances of a specific component class. When you call a component system’s [`update(deltaTime:)`](gkcomponentsystem/update(deltatime:).md) method, it forwards to the [`update(deltaTime:)`](gkcomponent/update(deltatime:).md) method of all the component objects it manages. Because a component system needs no knowledge of your game’s entity/component hierarchy, this option works well for games with complex object graphs.

For more information on Entity-Component architecture, read [`Entities and Components`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Performing Periodic Updates
- [func update(deltaTime: TimeInterval)](gkcomponent/update(deltatime:).md)
  Performs any custom periodic actions defined by the component subclass.
### Working with Entities
- [var entity: GKEntity?](gkcomponent/entity.md)
  The entity that owns this component.
- [func didAddToEntity()](gkcomponent/didaddtoentity.md)
  Notifies the component that it has been assigned to an entity.
- [func willRemoveFromEntity()](gkcomponent/willremovefromentity.md)
  Notifies the component that it has been removed from an entity.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GKAgent](gkagent.md)
- [GKSCNNodeComponent](gkscnnodecomponent.md)
- [GKSKNodeComponent](gksknodecomponent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class GKEntity](gkentity.md)
  An object relevant to gameplay, with functionality entirely provided by a collection of component objects.
- [class GKComponentSystem](gkcomponentsystem.md)
  Manages periodic update messages for all component objects of a specified class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponent)*