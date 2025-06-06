# SCNLayer

**Framework**: SceneKit  
**Kind**: class

A Core Animation layer that renders a SceneKit scene as its content.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class SCNLayer
```

#### Overview

Use this class to integrate 3D content rendered by SceneKit into a user interface composed of Core Animation layers. To provide content for the layer, assign an [`SCNScene`](scnscene.md) object to its [`scene`](scnlayer/scene.md) property.

Most of the methods and properties you use for working with a SceneKit layer are defined by the [`SCNSceneRenderer`](scnscenerenderer.md) protocol.

## Topics

### Specifying a Scene
- [var scene: SCNScene?](scnlayer/scene.md)
  The scene to be displayed in the layer.

## Relationships

### Inherits From
- [CAOpenGLLayer](../QuartzCore/CAOpenGLLayer.md)
### Conforms To
- [CAMediaTiming](../QuartzCore/CAMediaTiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [SCNSceneRenderer](scnscenerenderer.md)
- [SCNTechniqueSupport](scntechniquesupport.md)

## See Also

- [protocol SCNSceneRenderer](scnscenerenderer.md)
  Methods and properties common to the [`SCNView`](scnview.md), [`SCNLayer`](scnlayer.md), and [`SCNRenderer`](scnrenderer.md) classes.
- [protocol SCNSceneRendererDelegate](scnscenerendererdelegate.md)
  Methods your app can implement to participate in SceneKit’s animation loop or perform additional rendering.
- [class SCNRenderer](scnrenderer.md)
  A renderer for displaying a SceneKit scene in an existing Metal workflow or OpenGL context.
- [class SCNHitTestResult](scnhittestresult.md)
  Information about the result of a scene-space or view-space search for scene elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlayer)*