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

- [Providing 3D Virtual Content with SceneKit](providing-3d-virtual-content-with-scenekit.md)
  Use SceneKit to add realistic three-dimensional objects to your AR experience.
- [var scene: SCNScene](arscnview/scene.md)
  The SceneKit scene to be displayed in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/session)*