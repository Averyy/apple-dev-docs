# ARSCNDebugOptions

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Options for drawing overlay content to aid debugging of AR tracking in a SceneKit view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
typealias ARSCNDebugOptions = SCNDebugOptions
```

```c
typedef SCNDebugOptions ARSCNDebugOptions;
```

## Discussion

To use these debugging overlays, add them to the option set in the view’s [`debugOptions`](../SceneKit/scnscenerenderer/debugoptions.md) property (inherited from the [`SCNView`](../SceneKit/scnview.md) class).

## Topics

### AR Debugging Overlays
- [ARSCNDebugOptionShowWorldOrigin](./arscndebugoptionshowworldorigin.md)
  Display a coordinate axis visualization indicating the position and orientation of the AR world coordinate system.
- [ARSCNDebugOptionShowFeaturePoints](./arscndebugoptionshowfeaturepoints.md)
  Display a point cloud showing intermediate results of the scene analysis that ARKit uses to track device position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscndebugoptions)*