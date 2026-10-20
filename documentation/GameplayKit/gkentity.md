# GKEntity

**Framework**: GameplayKit  
**Kind**: class  
**Role**: Class

An object relevant to gameplay, with functionality entirely provided by a collection of component objects.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKEntity
```

```objc
@interface GKEntity : NSObject
```

#### Overview

A [`GKEntity`](./gkentity.md) object represents an entity in games with Entity-Component architecture. In this design, an *entity* is a general type for objects relevant to the game. Entities typically define no functionality of their own—instead, you define an entity’s features through composition, by adding *components* that each handle specific aspects of an entity’s behavior in a general way. Because components ([`GKComponent`](./gkcomponent.md) subclasses) are general and reusable, you can add many kinds of entities to a game by combining components in different ways, without needing to design new entity classes.

For more information on Entity-Component architecture, read [Entities and Components](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating an Entity
- [init()](./gkentity/init%28%29.md)
  Initializes a new entity object.
### Managing an Entity’s List of Components
- [var components: [GKComponent]](./gkentity/components.md)
  The entity’s list of components.
- [func addComponent(GKComponent)](./gkentity/addcomponent%28_%29.md)
  Adds a component to the entity.
### Performing Periodic Updates
- [func update(deltaTime: TimeInterval)](./gkentity/update%28deltatime%29.md)
  Performs periodic updates for each of the entity’s components.
### Instance Methods
- [func component<ComponentType>(ofType: ComponentType.Type) -> ComponentType?](./gkentity/component%28oftype%29.md)
- [func removeComponent<ComponentType>(ofType: ComponentType.Type)](./gkentity/removecomponent%28oftype%29.md)
### Initializers
- [init?(coder: NSCoder)](./gkentity/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Entities and Components
- [class GKComponent](./gkcomponent.md)
  The abstract superclass for creating objects that add specific gameplay functionality to an entity.
- [class GKComponentSystem](./gkcomponentsystem.md)
  Manages periodic update messages for all component objects of a specified class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkentity)*