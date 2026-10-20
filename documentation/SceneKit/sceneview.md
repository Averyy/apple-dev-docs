# SceneView

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

A SwiftUI view for displaying 3D SceneKit content.

**Availability**:
- iOS 14.0+ - Deprecated in 26.0
- iPadOS 14.0+ - Deprecated in 26.0
- Mac Catalyst 14.0+ - Deprecated in 26.0
- macOS 11.0+ - Deprecated in 26.0
- tvOS 14.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 7.0+ - Deprecated in 26.0

## Declaration

```swift
@MainActor
@preconcurrency struct SceneView
```

## Topics

### Creating a Scene View
- [init(scene: SCNScene?, pointOfView: SCNNode?, options: SceneView.Options, preferredFramesPerSecond: Int, antialiasingMode: SCNAntialiasingMode, delegate: (any SCNSceneRendererDelegate)?, technique: SCNTechnique?)](./sceneview/init%28scene,pointofview,options,preferredframespersecond,antialiasingmode,delegate,technique%29.md)
- [SceneView.Options](./sceneview/options.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Essentials
- [class SCNScene](./scnscene.md)
  A container for the node hierarchy and global properties that together form a displayable 3D scene.
- [class SCNView](./scnview.md)
  A view for displaying 3D SceneKit content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/sceneview)*