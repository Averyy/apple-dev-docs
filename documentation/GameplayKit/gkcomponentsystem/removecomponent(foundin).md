# removeComponent(foundIn:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Removes any instances of the component system’s component class in the specified entity from the component system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func removeComponent(foundIn entity: GKEntity)
```

```objc
- (void) removeComponentWithEntity:(GKEntity *) entity;
```

## Discussion

This method examines the [`components`](../gkentity/components.md) array of the specified entity, removing any components whose type matches the component system’s [`componentClass`](./componentclass.md) property from the component system. If those components are not in the component system, this method has no effect.

## Parameters

- `entity`: An entity.

## See Also

### Managing a List of Components
- [var componentClass: AnyClass](./componentclass.md)
  The class of components managed by the component system.
- [var components: [ComponentType]](./components.md)
  The component system’s list of components.
- [func addComponent(ComponentType)](./addcomponent%28_%29.md)
  Adds a component instance to the component system.
- [func addComponent(foundIn: GKEntity)](./addcomponent%28foundin%29.md)
  Adds any instances of the component system’s component class in the specified entity to the component system.
- [func removeComponent(ComponentType)](./removecomponent%28_%29.md)
  Removes the specified component instance from the component system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem/removecomponent(foundin:))*