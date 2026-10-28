# addComponent(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Adds a component instance to the component system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addComponent(_ component: ComponentType)
```

```objc
- (void) addComponent:(ComponentType) component;
```

## Discussion

The component instance must be of the same [`GKComponent`](../gkcomponent.md) subclass specified by the [`componentClass`](./componentclass.md) property.

## Parameters

- `component`: An instance of a [`GKComponent`](../gkcomponent.md) subclass.

## See Also

### Managing a List of Components
- [var componentClass: AnyClass](./componentclass.md)
  The class of components managed by the component system.
- [var components: [ComponentType]](./components.md)
  The component system’s list of components.
- [func addComponent(foundIn: GKEntity)](./addcomponent%28foundin%29.md)
  Adds any instances of the component system’s component class in the specified entity to the component system.
- [func removeComponent(ComponentType)](./removecomponent%28_%29.md)
  Removes the specified component instance from the component system.
- [func removeComponent(foundIn: GKEntity)](./removecomponent%28foundin%29.md)
  Removes any instances of the component system’s component class in the specified entity from the component system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem/addcomponent(_:))*