# session

**Framework**: ARKit  
**Kind**: property

The AR session that manages motion tracking and camera image processing for the view’s contents.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var session: ARSession { get set }
```

#### Discussion

A view creates its own session object; use this property to access and configure the view’s session.

## See Also

- [Providing 2D Virtual Content with SpriteKit](providing-2d-virtual-content-with-spritekit.md)
  Use SpriteKit to place two-dimensional images in 3D space in your AR experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskview/session)*