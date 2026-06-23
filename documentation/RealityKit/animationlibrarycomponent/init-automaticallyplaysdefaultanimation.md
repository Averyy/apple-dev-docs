# init(automaticallyPlaysDefaultAnimation:)

**Framework**: RealityKit  
**Kind**: init

Creates an empty animation library.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(automaticallyPlaysDefaultAnimation: Bool)
```

#### Example

```swift
var library = AnimationLibraryComponent(automaticallyPlaysDefaultAnimation: true)
library.animations["walk"] = walkAnimation
library.defaultKey = "walk"
entity.components.set(library)
```

## Parameters

- `automaticallyPlaysDefaultAnimation`: Whether to automatically play the default animation when the entity is added to a scene and enabled. When `true`, the animation system plays the default animation automatically. When `false`, animations require manual playback. See [`automaticallyPlaysDefaultAnimation`](animationlibrarycomponent/automaticallyplaysdefaultanimation.md) for details.

## See Also

- [var automaticallyPlaysDefaultAnimation: Bool](animationlibrarycomponent/automaticallyplaysdefaultanimation.md)
  Whether to automatically play the default animation when the entity is added to a scene and enabled. Default value is false, meaning the default animation will not be automatically played by default. This value can only be set when initializing `AnimationLibraryComponent`
- [init(animations: [String : AnimationResource], automaticallyPlaysDefaultAnimation: Bool)](animationlibrarycomponent/init(animations:automaticallyplaysdefaultanimation:).md)
  Creates an animation library from a dictionary that associates an animation’s data with its name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/init(automaticallyplaysdefaultanimation:))*