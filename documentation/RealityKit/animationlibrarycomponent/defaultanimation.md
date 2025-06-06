# defaultAnimation

**Framework**: RealityKit  
**Kind**: property

The default animation resource.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var defaultAnimation: AnimationResource? { get }
```

#### Discussion

The component looks up the resource by key if [`defaultKey`](animationlibrarycomponent/defaultkey.md) is non-`nil` and the library contains an animation that the key identifies. Otherwise, the component returns the first entry in the library.

## See Also

- [var animations: AnimationLibraryComponent.AnimationCollection](animationlibrarycomponent/animations.md)
  The collection of animations an entity can play.
- [var unkeyedResources: [AnimationResource]?](animationlibrarycomponent/unkeyedresources.md)
  The library’s animation resources that don’t have a queryable name.
- [var defaultKey: String?](animationlibrarycomponent/defaultkey.md)
  The name of the default animation resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/defaultanimation)*