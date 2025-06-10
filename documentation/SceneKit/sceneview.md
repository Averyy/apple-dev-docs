# SceneView

**Framework**: SceneKit  
**Kind**: struct

A SwiftUI view for displaying 3D SceneKit content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency struct SceneView
```

## Topics

### Creating a Scene View
- [init(scene: SCNScene?, pointOfView: SCNNode?, options: SceneView.Options, preferredFramesPerSecond: Int, antialiasingMode: SCNAntialiasingMode, delegate: (any SCNSceneRendererDelegate)?, technique: SCNTechnique?)](sceneview/init(scene:pointofview:options:preferredframespersecond:antialiasingmode:delegate:technique:).md)
- [SceneView.Options](sceneview/options.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [class SCNScene](scnscene.md)
  A container for the node hierarchy and global properties that together form a displayable 3D scene.
- [class SCNView](scnview.md)
  A view for displaying 3D SceneKit content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/sceneview)*