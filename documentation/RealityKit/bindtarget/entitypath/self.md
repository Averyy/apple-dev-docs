# self

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A bind target for the entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var `self`: BindTarget { get }
```

#### Discussion

This property represents a bind path within an [`AnimationView`](../../animationview.md) to redirect the view’s [`source`](../../blendtreesourcenode/source.md) animation to a different scene.

## See Also

### Accessing a bind target
- [var jointTransforms: BindTarget](./jointtransforms.md)
  A bind target for the entity’s joint transforms.
- [var transform: BindTarget](./transform.md)
  A bind target for the entity’s transform.
- [func parameter(String) -> BindTarget](./parameter%28_%29.md)
  Provides a bind target for a particular animated property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindtarget/entitypath/self)*