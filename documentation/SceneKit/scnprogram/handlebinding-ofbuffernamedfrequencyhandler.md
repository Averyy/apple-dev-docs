# handleBinding(ofBufferNamed:frequency:handler:)

**Framework**: SceneKit  
**Kind**: method

Registers a block for SceneKit to call at render time for binding a Metal buffer to the shader program.

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
func handleBinding(ofBufferNamed name: String, frequency: SCNBufferFrequency, handler block: @escaping SCNBufferBindingBlock)
```

#### Discussion

Use this method to associate a block with a Metal shader program to handle setup of a buffer used in that shader. SceneKit calls your block before rendering any objects whose [`program`](scnshadable/program.md) property is set to this [`SCNProgram`](scnprogram.md) object. In the block, use the [`writeBytes(_:count:)`](scnbufferstream/writebytes(_:count:).md) method to provide data for the buffer.

## Parameters

- `name`: The name identifying the buffer in Metal shader source code.
- `frequency`: An option specifying whether SceneKit calls the block only once per rendered frame or more frequently (for example, once for each object to be rendered).
- `block`: A block to be run when SceneKit prepares for rendering with the Metal shader.

## See Also

- [enum SCNBufferFrequency](scnbufferfrequency.md)
  Options for how often SceneKit should execute the binding handler you provide with the [`handleBinding(ofBufferNamed:frequency:handler:)`](scnprogram/handlebinding(ofbuffernamed:frequency:handler:).md) method.
- [typealias SCNBufferBindingBlock](scnbufferbindingblock.md)
  A block SceneKit calls at render time for working with buffers in a Metal shader, used by the [`handleBinding(ofBufferNamed:frequency:handler:)`](scnprogram/handlebinding(ofbuffernamed:frequency:handler:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/handlebinding(ofbuffernamed:frequency:handler:))*