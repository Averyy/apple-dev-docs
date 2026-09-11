# shouldClipSelf

**Framework**: RealityKit  
**Kind**: property

Controls whether the entity itself is clipped by this component’s bounds.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var shouldClipSelf: Bool
```

#### Discussion

When `true`, the entity’s own geometry is clipped by the bounding volume. When `false`, only child entities are affected (if `shouldClipChildren` is `true`).

## See Also

- [var shouldClipChildren: Bool](clippingcomponent/shouldclipchildren.md)
  Controls whether child entities are clipped by this component’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingcomponent/shouldclipself)*