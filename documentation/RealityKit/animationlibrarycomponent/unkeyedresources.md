# unkeyedResources

**Framework**: RealityKit  
**Kind**: property

The library’s animation resources that don’t have a queryable name.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var unkeyedResources: [AnimationResource]? { get }
```

#### Return Value

An array of the animation resources that don’t have a key; otherwise, `nil`.

## See Also

- [var animations: AnimationLibraryComponent.AnimationCollection](animationlibrarycomponent/animations.md)
  The collection of animations an entity can play.
- [var defaultAnimation: AnimationResource?](animationlibrarycomponent/defaultanimation.md)
  The default animation resource.
- [var defaultKey: String?](animationlibrarycomponent/defaultkey.md)
  The name of the default animation resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/unkeyedresources)*