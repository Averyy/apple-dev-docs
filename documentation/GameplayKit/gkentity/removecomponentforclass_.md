# removeComponentForClass:

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Removes the component of the specified class from the entity.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
- (void) removeComponentForClass:(Class) componentClass;
```

#### Discussion

An entity’s [`components`](./components.md) list always has no more than one instance of any component class. If the entity does not contain a component of the specified class, this method does nothing.

## Parameters

- `componentClass`: The [`GKComponent`](../gkcomponent.md) subclass for which to return a component instance.

## See Also

### Managing an Entity’s List of Components
- [var components: [GKComponent]](./components.md)
  The entity’s list of components.
- [- componentForClass:](./componentforclass_.md)
  Returns the entity’s component for the specified component class.
- [func addComponent(GKComponent)](./addcomponent%28_%29.md)
  Adds a component to the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkentity/removecomponentforclass:)*