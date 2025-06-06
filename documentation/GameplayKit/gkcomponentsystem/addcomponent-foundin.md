# addComponent(foundIn:)

**Framework**: GameplayKit  
**Kind**: method

Adds any instances of the component system’s component class in the specified entity to the component system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addComponent(foundIn entity: GKEntity)
```

#### Discussion

This method examines the [`components`](gkentity/components.md) array of the specified entity, adding any components whose type matches the component system’s [`componentClass`](gkcomponentsystem/componentclass.md) property to the component system.

## Parameters

- `entity`: An entity.

## See Also

- [var componentClass: AnyClass](gkcomponentsystem/componentclass.md)
  The class of components managed by the component system.
- [var components: [ComponentType]](gkcomponentsystem/components.md)
  The component system’s list of components.
- [func addComponent(ComponentType)](gkcomponentsystem/addcomponent(_:).md)
  Adds a component instance to the component system.
- [func removeComponent(ComponentType)](gkcomponentsystem/removecomponent(_:).md)
  Removes the specified component instance from the component system.
- [func removeComponent(foundIn: GKEntity)](gkcomponentsystem/removecomponent(foundin:).md)
  Removes any instances of the component system’s component class in the specified entity from the component system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem/addcomponent(foundin:))*