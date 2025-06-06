# scene

**Framework**: Arkit  
**Kind**: property

The SceneKit scene to be displayed in the view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var scene: SCNScene { get set }
```

#### Discussion

> **Note**:  Unlike the parent [`SCNView`](https://developer.apple.com/documentation/SceneKit/SCNView) class, an [`ARSCNView`](arscnview.md) object requires a non-`nil` scene to display.

## See Also

- [Providing 3D Virtual Content with SceneKit](providing-3d-virtual-content-with-scenekit.md)
  Use SceneKit to add realistic three-dimensional objects to your AR experience.
- [var session: ARSession](arscnview/session.md)
  The AR session that manages motion tracking and camera image processing for the view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ARKit/arscnview/scene)*