# SCNTechniqueSupport

**Framework**: SceneKit  
**Kind**: protocol

The common interface for SceneKit objects that support multipass rendering using [`SCNTechnique`](scntechnique.md) objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol SCNTechniqueSupport : NSObjectProtocol
```

#### Overview

Techniques let you specify approaches to rendering a scene that involves multiple drawing passes. For example, you might create a technique that uses a shader program to postprocess a rendered scene on the GPU, creating special effects such as color grading, screen-space ambient occlusion, or motion blur. Different SceneKit objects support techniques in different ways, summarized in Table 1.

| Class | Description |
| --- | --- |
| [`SCNView`](scnview.md), [`SCNLayer`](scnlayer.md) (macOS), [`SCNRenderer`](scnrenderer.md) | Apply effects whenever the scene is rendered. |
| [`SCNCamera`](scncamera.md) | Apply effects when the camera is the current point of view. |
| [`SCNLight`](scnlight.md) | Apply effects when the light is enabled. |

## Topics

### Specifying a Technique
- [var technique: SCNTechnique?](scntechniquesupport/technique.md)
  The technique SceneKit uses when rendering the object.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [SCNCamera](scncamera.md)
- [SCNLayer](scnlayer.md)
- [SCNLight](scnlight.md)
- [SCNRenderer](scnrenderer.md)
- [SCNView](scnview.md)

## See Also

- [protocol SCNShadable](scnshadable.md)
  Methods for customizing SceneKit’s rendering of geometry and materials using Metal or OpenGL shader programs.
- [class SCNProgram](scnprogram.md)
  A complete Metal or OpenGL shader program that replaces SceneKit’s rendering of a geometry or material.
- [protocol SCNBufferStream](scnbufferstream.md)
  An object that manages a Metal buffer used by a custom shader program.
- [class SCNTechnique](scntechnique.md)
  A specification for augmenting or postprocessing SceneKit’s rendering of a scene using additional drawing passes with custom Metal or OpenGL shaders.
- [protocol SCNNodeRendererDelegate](scnnoderendererdelegate.md)
  Methods you can implement to use your own custom Metal or OpenGL drawing code to render content for a node.
- [Postprocessing a Scene With Custom Symbols](postprocessing-a-scene-with-custom-symbols.md)
  Create visual effects in a scene by defining a rendering technique with custom symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntechniquesupport)*