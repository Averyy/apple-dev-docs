# components

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The component system’s list of components.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var components: [ComponentType] { get }
```

```objc
@property (nonatomic, retain, readonly) NSArray<GKComponent *> * components;
```

#### Discussion

Calling a method of the system’s component class forwards that message to every component in this array.

Important among component-specific messages is the [`update(deltaTime:)`](./update%28deltatime%29.md) method—call this method on a component system to perform per-frame updates for all the component instances it manages.

## See Also

### Managing a List of Components
- [var componentClass: AnyClass](./componentclass.md)
  The class of components managed by the component system.
- [func addComponent(ComponentType)](./addcomponent%28_%29.md)
  Adds a component instance to the component system.
- [func addComponent(foundIn: GKEntity)](./addcomponent%28foundin%29.md)
  Adds any instances of the component system’s component class in the specified entity to the component system.
- [func removeComponent(ComponentType)](./removecomponent%28_%29.md)
  Removes the specified component instance from the component system.
- [func removeComponent(foundIn: GKEntity)](./removecomponent%28foundin%29.md)
  Removes any instances of the component system’s component class in the specified entity from the component system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem/components)*