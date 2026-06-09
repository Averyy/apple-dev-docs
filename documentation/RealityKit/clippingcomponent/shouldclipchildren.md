# shouldClipChildren

**Framework**: RealityKit  
**Kind**: property

Controls whether child entities are clipped by this component’s bounds.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var shouldClipChildren: Bool
```

#### Discussion

When `true`, all descendant entities in the hierarchy will be clipped to this entity’s clipping bounds.

When `false`, only the entity with this component is affected (if `shouldClipSelf` is `true`).

## See Also

- [var shouldClipSelf: Bool](clippingcomponent/shouldclipself.md)
  Controls whether the entity itself is clipped by this component’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingcomponent/shouldclipchildren)*