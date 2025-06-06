# SCNNodeRendererDelegate

**Framework**: SceneKit  
**Kind**: protocol

Methods you can implement to use your own custom Metal or OpenGL drawing code to render content for a node.

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
protocol SCNNodeRendererDelegate : NSObjectProtocol
```

#### Overview

Typically, you use a node renderer delegate to perform custom rendering that is anchored at a location in the scene. For example, you can attach a node with a renderer delegate to part of a scene in order to add a special effect rendered using your own Metal or OpenGL drawing code, such as a fluid simulation. To provide a renderer delegate for an [`SCNNode`](scnnode.md) object, use its [`rendererDelegate`](scnnode/rendererdelegate.md) property.

SceneKit performs no rendering of its own for a node with a render delegate, so this protocol is not appropriate for customizing SceneKit’s rendering of geometry and materials. Instead, use methods in the [`SCNShadable`](scnshadable.md) protocol to extend SceneKit’s rendering using shader programs written in the Metal shading language or the OpenGL Shading Language (GLSL).

## Topics

### Customizing the Rendering of a Node
- [func renderNode(SCNNode, renderer: SCNRenderer, arguments: [String : Any])](scnnoderendererdelegate/rendernode(_:renderer:arguments:).md)
  Tells the delegate to perform rendering for a node.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol SCNShadable](scnshadable.md)
  Methods for customizing SceneKit’s rendering of geometry and materials using Metal or OpenGL shader programs.
- [class SCNProgram](scnprogram.md)
  A complete Metal or OpenGL shader program that replaces SceneKit’s rendering of a geometry or material.
- [protocol SCNBufferStream](scnbufferstream.md)
  An object that manages a Metal buffer used by a custom shader program.
- [class SCNTechnique](scntechnique.md)
  A specification for augmenting or postprocessing SceneKit’s rendering of a scene using additional drawing passes with custom Metal or OpenGL shaders.
- [protocol SCNTechniqueSupport](scntechniquesupport.md)
  The common interface for SceneKit objects that support multipass rendering using [`SCNTechnique`](scntechnique.md) objects.
- [Postprocessing a Scene With Custom Symbols](postprocessing-a-scene-with-custom-symbols.md)
  Create visual effects in a scene by defining a rendering technique with custom symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnoderendererdelegate)*