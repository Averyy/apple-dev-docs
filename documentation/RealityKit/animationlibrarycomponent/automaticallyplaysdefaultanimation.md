# automaticallyPlaysDefaultAnimation

**Framework**: RealityKit  
**Kind**: property

Whether to automatically play the default animation when the entity is added to a scene and enabled. Default value is false, meaning the default animation will not be automatically played by default. This value can only be set when initializing `AnimationLibraryComponent`

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var automaticallyPlaysDefaultAnimation: Bool { get }
```

#### Return Value

- `true` if automatically play default animation is enabled
- `false` if automatically play default animation is disabled

#### Discussion

When set to `true`, the animation system automatically plays the default animation when the entity is added to a scene and enabled. The animation that auto-plays is determined by [`defaultKey`](animationlibrarycomponent/defaultkey.md). If `defaultKey` is set, the system plays the animation stored under that key. If `defaultKey` is not set, the system plays the first animation in the library. If the library contains no animations, auto-play has no effect.

This is useful for background objects with looping animations, idle character states, or any entity whose animation should start without requiring code.

When set to `false`, animations require manual playback using [`playAnimation(_:transitionDuration:startsPaused:)`](entity/playanimation(_:transitionduration:startspaused:).md). Use manual playback when you need to control timing, pass custom parameters, or coordinate animation start with other game logic.

Disabling the entity or removing the `AnimationLibraryComponent` will stop any auto-playing animation.

#### Example

```swift
var library = AnimationLibraryComponent(automaticallyPlaysDefaultAnimation: true)
library["idle"] = idleAnimation
library.defaultKey = "idle"
entity.components.set(library)
// Animation plays automatically when the entity is added to a scene and enabled
```

## See Also

- [init(automaticallyPlaysDefaultAnimation: Bool)](animationlibrarycomponent/init(automaticallyplaysdefaultanimation:).md)
  Creates an empty animation library.
- [init(animations: [String : AnimationResource], automaticallyPlaysDefaultAnimation: Bool)](animationlibrarycomponent/init(animations:automaticallyplaysdefaultanimation:).md)
  Creates an animation library from a dictionary that associates an animation’s data with its name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/automaticallyplaysdefaultanimation)*