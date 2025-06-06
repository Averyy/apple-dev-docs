# defaultKey

**Framework**: RealityKit  
**Kind**: property

The name of the default animation resource.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var defaultKey: String? { get set }
```

#### Discussion

Returns `nil` if you don’t set a default animation, or if the component can’t find it.

## See Also

- [var animations: AnimationLibraryComponent.AnimationCollection](animationlibrarycomponent/animations.md)
  The collection of animations an entity can play.
- [var unkeyedResources: [AnimationResource]?](animationlibrarycomponent/unkeyedresources.md)
  The library’s animation resources that don’t have a queryable name.
- [var defaultAnimation: AnimationResource?](animationlibrarycomponent/defaultanimation.md)
  The default animation resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/defaultkey)*