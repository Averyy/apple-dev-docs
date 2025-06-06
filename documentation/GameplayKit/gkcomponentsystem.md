# GKComponentSystem

**Framework**: GameplayKit  
**Kind**: class

Manages periodic update messages for all component objects of a specified class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKComponentSystem<ComponentType> where ComponentType : GKComponent
```

#### Overview

A [`GKComponentSystem`](gkcomponentsystem.md) object manages periodic update messages for components in a game that uses Entity-Component architecture. Use a component system to perform per-frame logic for all components of a specific class without traversing your game’s object hierarchy to dispatch update messages.

Each [`GKComponentSystem`](gkcomponentsystem.md) object manages components of a specific [`GKComponent`](gkcomponent.md) subclass. You create a component system with the [`init(componentClass:)`](gkcomponentsystem/init(componentclass:).md) initializer, specifying the component class it will work with. Then, you register the components used by the entities in your game with the [`addComponent(_:)`](gkcomponentsystem/addcomponent(_:).md) or [`addComponent(foundIn:)`](gkcomponentsystem/addcomponent(foundin:).md) methods. The component system will then forward any component-specific messages it receives to all registered instances of its component class.

The most important of the component-specific messages is the [`update(deltaTime:)`](gkcomponentsystem/update(deltatime:).md) method. Call this method from your game’s update/render loop—that is, from a method such as [`update(_:)`](https://developer.apple.com/documentation/SpriteKit/SKScene/update(_:)) (SpriteKit) or [`renderer(_:updateAtTime:)`](https://developer.apple.com/documentation/SceneKit/SCNSceneRendererDelegate/renderer(_:updateAtTime:)) (SceneKit), or from a [`CADisplayLink`](https://developer.apple.com/documentation/QuartzCore/CADisplayLink) (iOS) or [`CVDisplayLink`](https://developer.apple.com/documentation/CoreVideo/CVDisplayLink) (macOS) timer in a custom rendering engine. The component system then forwards to the [`update(deltaTime:)`](gkcomponent/update(deltatime:).md) method of all the [`GKComponent`](gkcomponent.md) subclass instances it manages, allowing those objects to perform per-frame update logic.

For more information on Entity-Component architecture, read [`Entities and Components`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a Component System
- [init(componentClass: AnyClass)](gkcomponentsystem/init(componentclass:).md)
  Initializes a component system to manage components of the specified class.
### Managing a List of Components
- [var componentClass: AnyClass](gkcomponentsystem/componentclass.md)
  The class of components managed by the component system.
- [var components: [ComponentType]](gkcomponentsystem/components.md)
  The component system’s list of components.
- [func addComponent(ComponentType)](gkcomponentsystem/addcomponent(_:).md)
  Adds a component instance to the component system.
- [func addComponent(foundIn: GKEntity)](gkcomponentsystem/addcomponent(foundin:).md)
  Adds any instances of the component system’s component class in the specified entity to the component system.
- [func removeComponent(ComponentType)](gkcomponentsystem/removecomponent(_:).md)
  Removes the specified component instance from the component system.
- [func removeComponent(foundIn: GKEntity)](gkcomponentsystem/removecomponent(foundin:).md)
  Removes any instances of the component system’s component class in the specified entity from the component system.
### Performing Periodic Updates
- [func update(deltaTime: TimeInterval)](gkcomponentsystem/update(deltatime:).md)
  Tells all component instances managed by the system to perform their custom periodic actions.
### Accessing Components With Subscript Syntax
- [subscript(Int) -> ComponentType](gkcomponentsystem/subscript(_:).md)
  Returns the component at the specified index in the system’s list of components.
### Instance Methods
- [func classForGenericArgument(at: Int) -> AnyClass](gkcomponentsystem/classforgenericargument(at:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSFastEnumeration](../Foundation/NSFastEnumeration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKEntity](gkentity.md)
  An object relevant to gameplay, with functionality entirely provided by a collection of component objects.
- [class GKComponent](gkcomponent.md)
  The abstract superclass for creating objects that add specific gameplay functionality to an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem)*