# scene

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The SceneKit scene to be displayed in the view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var scene: SCNScene { get set }
```

```objc
@property (nonatomic, strong) SCNScene * scene;
```

#### Discussion

> **Note**:  Unlike the parent [`SCNView`](../../SceneKit/scnview.md) class, an [`ARSCNView`](../arscnview.md) object requires a non-`nil` scene to display.

## See Also

### Essentials
- [Providing 3D Virtual Content with SceneKit](../providing-3d-virtual-content-with-scenekit.md)
  Use SceneKit to add realistic three-dimensional objects to your AR experience.
- [var session: ARSession](./session.md)
  The AR session that manages motion tracking and camera image processing for the view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/scene)*