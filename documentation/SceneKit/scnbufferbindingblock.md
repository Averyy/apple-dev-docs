# SCNBufferBindingBlock

**Framework**: SceneKit  
**Kind**: typealias  
**Role**: Type Alias

A block SceneKit calls at render time for working with buffers in a Metal shader, used by the [`handleBinding(ofBufferNamed:frequency:handler:)`](./scnprogram/handlebinding%28ofbuffernamed,frequency,handler%29.md) method.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
typealias SCNBufferBindingBlock = (any SCNBufferStream, SCNNode, any SCNShadable, SCNRenderer) -> Void
```

```c
typedef void (^)(id<SCNBufferStream>, SCNNode *, id<SCNShadable>, SCNRenderer *) SCNBufferBindingBlock;
```

#### Discussion

The block takes the following parameters:

- **buffer**: An object that provides write access to the buffer. Use the [`writeBytes(_:count:)`](./scnbufferstream/writebytes%28_,count%29.md) method on this object to write data for use by the shader.
- **node**: The node to be rendered using the shader program.
- **shadable**: The material or geometry to be rendered using the shader program.
- **renderer**: The view (or other SceneKit renderer) responsible for rendering.

## See Also

### Providing Input for Metal Shaders
- [func handleBinding(ofBufferNamed: String, frequency: SCNBufferFrequency, handler: SCNBufferBindingBlock)](./scnprogram/handlebinding%28ofbuffernamed,frequency,handler%29.md)
  Registers a block for SceneKit to call at render time for binding a Metal buffer to the shader program.
- [enum SCNBufferFrequency](./scnbufferfrequency.md)
  Options for how often SceneKit should execute the binding handler you provide with the [`handleBinding(ofBufferNamed:frequency:handler:)`](./scnprogram/handlebinding%28ofbuffernamed,frequency,handler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbufferbindingblock)*