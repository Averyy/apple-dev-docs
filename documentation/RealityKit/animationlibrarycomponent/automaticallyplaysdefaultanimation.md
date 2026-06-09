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

When set to `true`, the animation system automatically plays the default animation when the entity is added to a scene and enabled. The default animation is determined by [`defaultKey`](animationlibrarycomponent/defaultkey.md) or, if that’s not set, the first animation in the library.

When set to `false`, animations require manual playback using [`playAnimation(_:transitionDuration:startsPaused:)`](entity/playanimation(_:transitionduration:startspaused:).md).

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
- [init(dictionaryLiteral: (String, AnimationResource)..., automaticallyPlaysDefaultAnimation: Bool)](animationlibrarycomponent/init(dictionaryliteral:automaticallyplaysdefaultanimation:).md)
  Creates an animation library from a variadic list of key-value pairs


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/automaticallyplaysdefaultanimation)*