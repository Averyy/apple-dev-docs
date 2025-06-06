# update(deltaTime:)

**Framework**: GameplayKit  
**Kind**: method

Performs any custom periodic actions defined by the component subclass.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func update(deltaTime seconds: TimeInterval)
```

#### Discussion

Override this method to implement per-frame logic specific to your component class. GameplayKit calls this method when you call the [`update(deltaTime:)`](gkentity/update(deltatime:).md) method of the entity owning a component, or when you call the [`update(deltaTime:)`](gkcomponentsystem/update(deltatime:).md) method of a [`GKComponentSystem`](gkcomponentsystem.md) object that manages all components of a specific [`GKComponent`](gkcomponent.md) subclass. Typically, you call one of those methods in response to a per-frame game loop method such as [`update(_:)`](https://developer.apple.com/documentation/SpriteKit/SKScene/update(_:)) (SpriteKit) or [`renderer(_:updateAtTime:)`](https://developer.apple.com/documentation/SceneKit/SCNSceneRendererDelegate/renderer(_:updateAtTime:)) (SceneKit).

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `seconds`: The time step to use for any time-dependent actions performed by this method (typically, the elapsed time since the previous call to this method).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponent/update(deltatime:))*