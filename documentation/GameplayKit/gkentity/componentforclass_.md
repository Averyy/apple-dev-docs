# componentForClass:

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Returns the entity’s component for the specified component class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
- (GKComponent *) componentForClass:(Class) componentClass;
```

#### Return Value

The component instance for the specified class, or `nil` if the entity has no components of that class.

#### Discussion

An entity’s [`components`](./components.md) list always has no more than one instance of any component class. Use this method to retrieve a component instance when all you know is that the entity contains a component of a particular class.

## Parameters

- `componentClass`: The [`GKComponent`](../gkcomponent.md) subclass for which to return a component instance.

## See Also

### Managing an Entity’s List of Components
- [var components: [GKComponent]](./components.md)
  The entity’s list of components.
- [func addComponent(GKComponent)](./addcomponent%28_%29.md)
  Adds a component to the entity.
- [- removeComponentForClass:](./removecomponentforclass_.md)
  Removes the component of the specified class from the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkentity/componentforclass:)*