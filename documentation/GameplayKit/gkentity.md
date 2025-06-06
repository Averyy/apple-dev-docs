# GKEntity

**Framework**: GameplayKit  
**Kind**: class

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

#### Overview

A [`GKEntity`](gkentity.md) object represents an entity in games with Entity-Component architecture. In this design, an  is a general type for objects relevant to the game. Entities typically define no functionality of their own—instead, you define an entity’s features through composition, by adding  that each handle specific aspects of an entity’s behavior in a general way. Because components ([`GKComponent`](gkcomponent.md) subclasses) are general and reusable, you can add many kinds of entities to a game by combining components in different ways, without needing to design new entity classes.

For more information on Entity-Component architecture, read [`Entities and Components`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating an Entity
- [init()](gkentity/init.md)
  Initializes a new entity object.
### Managing an Entity’s List of Components
- [var components: [GKComponent]](gkentity/components.md)
  The entity’s list of components.
- [func addComponent(GKComponent)](gkentity/addcomponent(_:).md)
  Adds a component to the entity.
### Performing Periodic Updates
- [func update(deltaTime: TimeInterval)](gkentity/update(deltatime:).md)
  Performs periodic updates for each of the entity’s components.
### Instance Methods
- [func component<ComponentType>(ofType: ComponentType.Type) -> ComponentType?](gkentity/component(oftype:).md)
- [func removeComponent<ComponentType>(ofType: ComponentType.Type)](gkentity/removecomponent(oftype:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

- [class GKComponent](gkcomponent.md)
  The abstract superclass for creating objects that add specific gameplay functionality to an entity.
- [class GKComponentSystem](gkcomponentsystem.md)
  Manages periodic update messages for all component objects of a specified class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkentity)*