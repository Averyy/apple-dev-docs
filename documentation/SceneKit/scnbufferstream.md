# SCNBufferStream

**Framework**: SceneKit  
**Kind**: protocol

An object that manages a Metal buffer used by a custom shader program.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol SCNBufferStream : NSObjectProtocol
```

#### Overview

Your app does not define classes that implement this protocol. Instead, you use the [`SCNProgram`](scnprogram.md) method [`handleBinding(ofBufferNamed:frequency:handler:)`](scnprogram/handlebinding(ofbuffernamed:frequency:handler:).md) to register a block to be called by SceneKit. In that block, SceneKit provides a buffer stream object that you can use to write data to the buffer.

## Topics

### Writing Data to a Buffer
- [func writeBytes(UnsafeRawPointer, count: Int)](scnbufferstream/writebytes(_:count:).md)
  Copies the specified data bytes into the underlying Metal buffer for use by a shader.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol SCNShadable](scnshadable.md)
  Methods for customizing SceneKit’s rendering of geometry and materials using Metal or OpenGL shader programs.
- [class SCNProgram](scnprogram.md)
  A complete Metal or OpenGL shader program that replaces SceneKit’s rendering of a geometry or material.
- [class SCNTechnique](scntechnique.md)
  A specification for augmenting or postprocessing SceneKit’s rendering of a scene using additional drawing passes with custom Metal or OpenGL shaders.
- [protocol SCNTechniqueSupport](scntechniquesupport.md)
  The common interface for SceneKit objects that support multipass rendering using [`SCNTechnique`](scntechnique.md) objects.
- [protocol SCNNodeRendererDelegate](scnnoderendererdelegate.md)
  Methods you can implement to use your own custom Metal or OpenGL drawing code to render content for a node.
- [Postprocessing a Scene With Custom Symbols](postprocessing-a-scene-with-custom-symbols.md)
  Create visual effects in a scene by defining a rendering technique with custom symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbufferstream)*