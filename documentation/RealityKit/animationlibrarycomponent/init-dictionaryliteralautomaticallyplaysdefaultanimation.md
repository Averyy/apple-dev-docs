# init(dictionaryLiteral:automaticallyPlaysDefaultAnimation:)

**Framework**: RealityKit  
**Kind**: init

Creates an animation library from a variadic list of key-value pairs

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(dictionaryLiteral elements: (String, AnimationResource)..., automaticallyPlaysDefaultAnimation: Bool)
```

#### Discussion

Use the [`ExpressibleByDictionaryLiteral`](https://developer.apple.com/documentation/Swift/ExpressibleByDictionaryLiteral) initializer by directly assigning the library to a dictionary literal.

## Parameters

- `elements`: A list of key-value pairs that make up the dictionary. Each key is a unique animation name, and each value is an animation resource.
- `automaticallyPlaysDefaultAnimation`: Whether to automatically play the default animation when the entity is added to a scene and enabled. When `true`, the animation system plays the default animation automatically. When `false`, animations require manual playback. See [`automaticallyPlaysDefaultAnimation`](animationlibrarycomponent/automaticallyplaysdefaultanimation.md) for details.

## See Also

- [var automaticallyPlaysDefaultAnimation: Bool](animationlibrarycomponent/automaticallyplaysdefaultanimation.md)
  Whether to automatically play the default animation when the entity is added to a scene and enabled. Default value is false, meaning the default animation will not be automatically played by default. This value can only be set when initializing `AnimationLibraryComponent`
- [init(automaticallyPlaysDefaultAnimation: Bool)](animationlibrarycomponent/init(automaticallyplaysdefaultanimation:).md)
  Creates an empty animation library.
- [init(animations: [String : AnimationResource], automaticallyPlaysDefaultAnimation: Bool)](animationlibrarycomponent/init(animations:automaticallyplaysdefaultanimation:).md)
  Creates an animation library from a dictionary that associates an animation’s data with its name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/init(dictionaryliteral:automaticallyplaysdefaultanimation:))*