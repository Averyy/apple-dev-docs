# componentClass

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) Class componentClass;
```

## Discussion

Each [`GKComponentSystem`](../gkcomponentsystem.md) object manages components of a specific [`GKComponent`](../gkcomponent.md) subclass. You specify the component class to be used by a system when creating it with the [`init(componentClass:)`](./init%28componentclass%29.md) initializer. Afterward, you may add components to the system only if their type matches the system’s component class.

## See Also

### Managing a List of Components
- [var components: [ComponentType]](./components.md)
  The component system’s list of components.
- [func addComponent(ComponentType)](./addcomponent%28_%29.md)
  Adds a component instance to the component system.
- [func addComponent(foundIn: GKEntity)](./addcomponent%28foundin%29.md)
  Adds any instances of the component system’s component class in the specified entity to the component system.
- [func removeComponent(ComponentType)](./removecomponent%28_%29.md)
  Removes the specified component instance from the component system.
- [func removeComponent(foundIn: GKEntity)](./removecomponent%28foundin%29.md)
  Removes any instances of the component system’s component class in the specified entity from the component system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem/componentclass)*