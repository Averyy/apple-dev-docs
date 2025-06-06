# init(componentClass:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a component system to manage components of the specified class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(componentClass cls: AnyClass)
```

#### Return Value

A new component system.

#### Discussion

Each [`GKComponentSystem`](gkcomponentsystem.md) object manages components of a specific [`GKComponent`](gkcomponent.md) subclass, which you specify with the `class` parameter in this intializer. After initializing a component system, you may add components to it only if their type matches the system’s component class.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem/init(componentclass:))*