# update(deltaTime:)

**Framework**: GameplayKit  
**Kind**: method

Tells all component instances managed by the system to perform their custom periodic actions.

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

Typically, you call this method in response to a per-frame game loop method such as [`update(_:)`](https://developer.apple.com/documentation/SpriteKit/SKScene/update(_:)) (SpriteKit) or [`renderer(_:updateAtTime:)`](https://developer.apple.com/documentation/SceneKit/SCNSceneRendererDelegate/renderer(_:updateAtTime:)) (SceneKit). GameplayKit then forwards to the [`update(deltaTime:)`](gkcomponent/update(deltatime:).md) method of all [`GKComponent`](gkcomponent.md) subclass objects managed by the component system, allowing you to execute per-frame logic for each component instance in a deterministic order.

## Parameters

- `seconds`: The time step to use for any time-dependent actions to be performed by components (typically, the elapsed time since the previous call to this method).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem/update(deltatime:))*