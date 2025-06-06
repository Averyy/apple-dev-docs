# SCNBufferFrequency

**Framework**: SceneKit  
**Kind**: enum

Options for how often SceneKit should execute the binding handler you provide with the [`handleBinding(ofBufferNamed:frequency:handler:)`](scnprogram/handlebinding(ofbuffernamed:frequency:handler:).md) method.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SCNBufferFrequency
```

## Topics

### Constants
- [SCNBufferFrequency.perFrame](scnbufferfrequency/perframe.md)
  Execute the binding handler once for each frame to be rendered using the shader.
- [SCNBufferFrequency.perNode](scnbufferfrequency/pernode.md)
  Execute the binding handler once for each frame, for each node to be rendered using the shader.
- [SCNBufferFrequency.perShadable](scnbufferfrequency/pershadable.md)
  Execute the binding handler once for each frame, for each node, for each material or geometry to be rendered using the shader.
### Initializers
- [init?(rawValue: Int)](scnbufferfrequency/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func handleBinding(ofBufferNamed: String, frequency: SCNBufferFrequency, handler: SCNBufferBindingBlock)](scnprogram/handlebinding(ofbuffernamed:frequency:handler:).md)
  Registers a block for SceneKit to call at render time for binding a Metal buffer to the shader program.
- [typealias SCNBufferBindingBlock](scnbufferbindingblock.md)
  A block SceneKit calls at render time for working with buffers in a Metal shader, used by the [`handleBinding(ofBufferNamed:frequency:handler:)`](scnprogram/handlebinding(ofbuffernamed:frequency:handler:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbufferfrequency)*