# update(deltaTime:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Performs periodic updates for each of the entity’s components.

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

```objc
- (void) updateWithDeltaTime:(NSTimeInterval) seconds;
```

#### Discussion

At runtime, an entity/component-based game needs to dispatch periodic logic—from an update/render loop method such as [`update(_:)`](../../SpriteKit/skscene/update%28_%29.md) (SpriteKit) or [`renderer(_:updateAtTime:)`](../../SceneKit/scnscenerendererdelegate/renderer%28_,updateattime%29.md) (SceneKit), or a [`CADisplayLink`](../../QuartzCore/cadisplaylink.md) (iOS) or [`CVDisplayLink`](../../CoreVideo/cvdisplaylink.md) (macOS) timer in a custom rendering engine—to each of its components, so that each can perform component-specific update logic.

The [`GKEntity`](../gkentity.md) [`update(deltaTime:)`](./update%28deltatime%29.md) method is one of the two options GameplayKit provides for dispatching updates—this option is easy to implement in games with small numbers of entities and components. Call this method for each entity in your game, and each entity will in turn call the [`update(deltaTime:)`](../gkcomponent/update%28deltatime%29.md) method for each of its components.

The other option is to dispatch updates per-component, rather than per-entity, using a [`GKComponentSystem`](../gkcomponentsystem.md) object. Using a component system allows you to update all components of a specific component class in a deterministic order, without needing to traverse your game’s object graph and update each entity.

> **Note**:  If a component owned by an entity is a member of a component system, calling the entity’s [`update(deltaTime:)`](./update%28deltatime%29.md) method will not update that component.

## Parameters

- `seconds`: The time step to use for any time-dependent actions performed by this method (typically, the elapsed time since the previous call to this method).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkentity/update(deltatime:))*