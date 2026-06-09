# shouldClipSelf

**Framework**: RealityKit  
**Kind**: property

Controls whether the entity itself is clipped by this component’s bounds.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var shouldClipSelf: Bool
```

#### Discussion

When `true`, the entity’s own geometry is clipped by the bounding volume. When `false`, only child entities are affected (if `shouldClipChildren` is `true`).

## See Also

- [var shouldClipChildren: Bool](clippingprimitivecomponent/shouldclipchildren.md)
  Controls whether child entities are clipped by this component’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingprimitivecomponent/shouldclipself)*