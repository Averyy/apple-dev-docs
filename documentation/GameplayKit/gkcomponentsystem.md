# GKComponentSystem

**Framework**: GameplayKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface GKComponentSystem : NSObject
```

#### Overview

A [`GKComponentSystem`](./gkcomponentsystem.md) object manages periodic update messages for components in a game that uses Entity-Component architecture. Use a component system to perform per-frame logic for all components of a specific class without traversing your game’s object hierarchy to dispatch update messages.

Each [`GKComponentSystem`](./gkcomponentsystem.md) object manages components of a specific [`GKComponent`](./gkcomponent.md) subclass. You create a component system with the [`init(componentClass:)`](./gkcomponentsystem/init%28componentclass%29.md) initializer, specifying the component class it will work with. Then, you register the components used by the entities in your game with the [`addComponent(_:)`](./gkcomponentsystem/addcomponent%28_%29.md) or [`addComponent(foundIn:)`](./gkcomponentsystem/addcomponent%28foundin%29.md) methods. The component system will then forward any component-specific messages it receives to all registered instances of its component class.

The most important of the component-specific messages is the [`update(deltaTime:)`](./gkcomponentsystem/update%28deltatime%29.md) method. Call this method from your game’s update/render loop—that is, from a method such as [`update(_:)`](../SpriteKit/skscene/update%28_%29.md) (SpriteKit) or [`renderer(_:updateAtTime:)`](../SceneKit/scnscenerendererdelegate/renderer%28_,updateattime%29.md) (SceneKit), or from a [`CADisplayLink`](../QuartzCore/cadisplaylink.md) (iOS) or [`CVDisplayLink`](../CoreVideo/cvdisplaylink.md) (macOS) timer in a custom rendering engine. The component system then forwards to the [`update(deltaTime:)`](./gkcomponent/update%28deltatime%29.md) method of all the [`GKComponent`](./gkcomponent.md) subclass instances it manages, allowing those objects to perform per-frame update logic.

For more information on Entity-Component architecture, read [Entities and Components](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a Component System
- [init(componentClass: AnyClass)](./gkcomponentsystem/init%28componentclass%29.md)
  Initializes a component system to manage components of the specified class.
### Managing a List of Components
- [var componentClass: AnyClass](./gkcomponentsystem/componentclass.md)
  The class of components managed by the component system.
- [var components: [ComponentType]](./gkcomponentsystem/components.md)
  The component system’s list of components.
- [func addComponent(ComponentType)](./gkcomponentsystem/addcomponent%28_%29.md)
  Adds a component instance to the component system.
- [func addComponent(foundIn: GKEntity)](./gkcomponentsystem/addcomponent%28foundin%29.md)
  Adds any instances of the component system’s component class in the specified entity to the component system.
- [func removeComponent(ComponentType)](./gkcomponentsystem/removecomponent%28_%29.md)
  Removes the specified component instance from the component system.
- [func removeComponent(foundIn: GKEntity)](./gkcomponentsystem/removecomponent%28foundin%29.md)
  Removes any instances of the component system’s component class in the specified entity from the component system.
### Performing Periodic Updates
- [func update(deltaTime: TimeInterval)](./gkcomponentsystem/update%28deltatime%29.md)
  Tells all component instances managed by the system to perform their custom periodic actions.
### Accessing Components With Subscript Syntax
- [subscript(Int) -> ComponentType](./gkcomponentsystem/subscript%28_%29.md)
  Returns the component at the specified index in the system’s list of components.
### Instance Methods
- [func classForGenericArgument(at: Int) -> AnyClass](./gkcomponentsystem/classforgenericargument%28at%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSFastEnumeration](../Foundation/nsfastenumeration.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Entities and Components
- [class GKEntity](./gkentity.md)
  An object relevant to gameplay, with functionality entirely provided by a collection of component objects.
- [class GKComponent](./gkcomponent.md)
  The abstract superclass for creating objects that add specific gameplay functionality to an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem)*