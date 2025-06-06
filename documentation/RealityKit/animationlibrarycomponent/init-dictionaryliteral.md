# init(dictionaryLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates an animation library from a variadic list of key-value pairs.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(dictionaryLiteral elements: (String, AnimationResource)...)
```

#### Discussion

Use the [`ExpressibleByDictionaryLiteral`](https://developer.apple.com/documentation/Swift/ExpressibleByDictionaryLiteral) initializer by directly assigning the library to a dictionary literal.

```swift
let animationLibrary: AnimationLibraryComponent = [
    "idle": idleAnimation,
    "walk": walkAnimation
]
```

## Parameters

- `elements`: A list of key-value pairs that make up the dictionary.   Each key is a unique animation name, and each value is an animation resource.

## See Also

- [init()](animationlibrarycomponent/init.md)
  Creates an empty animation library.
- [init(animations: [String : AnimationResource])](animationlibrarycomponent/init(animations:).md)
  Creates an animation library from a dictionary that associates an animation’s data with its name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/init(dictionaryliteral:))*