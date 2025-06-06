# addComponent(_:)

**Framework**: GameplayKit  
**Kind**: method

Adds a component to the entity.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addComponent(_ component: GKComponent)
```

#### Discussion

You create components by subclassing [`GKEntity`](gkentity.md) to implement reusable behavior. Then, use this method to incorporate the behavior of a component class into that entity.

An entity’s [`components`](gkentity/components.md) list never has more than one instance of any component class—if the entity already contains a component of the same class as the `component` parameter, calling this method will replace that component.

## Parameters

- `component`: An instance of a   subclass.

## See Also

- [var components: [GKComponent]](gkentity/components.md)
  The entity’s list of components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkentity/addcomponent(_:))*