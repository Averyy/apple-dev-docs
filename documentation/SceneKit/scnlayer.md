# SCNLayer

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A Core Animation layer that renders a SceneKit scene as its content.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: OpenGL API deprecated, please use Metal instead. (Define SCN_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
class SCNLayer
```

```objc
@interface SCNLayer : CAOpenGLLayer
```

#### Overview

Use this class to integrate 3D content rendered by SceneKit into a user interface composed of Core Animation layers. To provide content for the layer, assign an [`SCNScene`](./scnscene.md) object to its [`scene`](./scnlayer/scene.md) property.

Most of the methods and properties you use for working with a SceneKit layer are defined by the [`SCNSceneRenderer`](./scnscenerenderer.md) protocol.

## Topics

### Specifying a Scene
- [var scene: SCNScene?](./scnlayer/scene.md)
  The scene to be displayed in the layer.

## Relationships

### Inherits From
- [CAOpenGLLayer](../QuartzCore/caopengllayer.md)
### Conforms To
- [CAMediaTiming](../QuartzCore/camediatiming.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [SCNSceneRenderer](./scnscenerenderer.md)
- [SCNTechniqueSupport](./scntechniquesupport.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Display and Interactivity
- [protocol SCNSceneRenderer](./scnscenerenderer.md)
  Methods and properties common to the [`SCNView`](./scnview.md), [`SCNLayer`](./scnlayer.md), and [`SCNRenderer`](./scnrenderer.md) classes.
- [protocol SCNSceneRendererDelegate](./scnscenerendererdelegate.md)
  Methods your app can implement to participate in SceneKit’s animation loop or perform additional rendering.
- [class SCNRenderer](./scnrenderer.md)
  A renderer for displaying a SceneKit scene in an existing Metal workflow or OpenGL context.
- [class SCNHitTestResult](./scnhittestresult.md)
  Information about the result of a scene-space or view-space search for scene elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlayer)*