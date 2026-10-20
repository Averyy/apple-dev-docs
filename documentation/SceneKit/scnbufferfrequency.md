# SCNBufferFrequency

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Options for how often SceneKit should execute the binding handler you provide with the [`handleBinding(ofBufferNamed:frequency:handler:)`](./scnprogram/handlebinding%28ofbuffernamed,frequency,handler%29.md) method.

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
enum SCNBufferFrequency
```

```c
enum SCNBufferFrequency : NSInteger;
```

## Topics

### Constants
- [SCNBufferFrequency.perFrame](./scnbufferfrequency/perframe.md)
  Execute the binding handler once for each frame to be rendered using the shader.
- [SCNBufferFrequency.perNode](./scnbufferfrequency/pernode.md)
  Execute the binding handler once for each frame, for each node to be rendered using the shader.
- [SCNBufferFrequency.perShadable](./scnbufferfrequency/pershadable.md)
  Execute the binding handler once for each frame, for each node, for each material or geometry to be rendered using the shader.
### Initializers
- [init?(rawValue: Int)](./scnbufferfrequency/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Providing Input for Metal Shaders
- [func handleBinding(ofBufferNamed: String, frequency: SCNBufferFrequency, handler: SCNBufferBindingBlock)](./scnprogram/handlebinding%28ofbuffernamed,frequency,handler%29.md)
  Registers a block for SceneKit to call at render time for binding a Metal buffer to the shader program.
- [typealias SCNBufferBindingBlock](./scnbufferbindingblock.md)
  A block SceneKit calls at render time for working with buffers in a Metal shader, used by the [`handleBinding(ofBufferNamed:frequency:handler:)`](./scnprogram/handlebinding%28ofbuffernamed,frequency,handler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbufferfrequency)*