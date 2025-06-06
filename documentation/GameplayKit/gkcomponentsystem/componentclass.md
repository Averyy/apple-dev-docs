# componentClass

**Framework**: GameplayKit  
**Kind**: property

The class of components managed by the component system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var componentClass: AnyClass { get }
```

#### Discussion

Each [`GKComponentSystem`](gkcomponentsystem.md) object manages components of a specific [`GKComponent`](gkcomponent.md) subclass. You specify the component class to be used by a system when creating it with the [`init(componentClass:)`](gkcomponentsystem/init(componentclass:).md) initializer. Afterward, you may add components to the system only if their type matches the system’s component class.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem/componentclass)*