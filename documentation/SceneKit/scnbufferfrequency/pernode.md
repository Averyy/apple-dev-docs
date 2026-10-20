# SCNBufferFrequency.perNode

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

Execute the binding handler once for each frame, for each node to be rendered using the shader.

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
case perNode
```

```c
SCNBufferFrequencyPerNode
```

#### Discussion

Use this option when the contents of the buffer should be uniform across multiple geometries or materials, but specific to each node rendered using the shader. For example, a node-specific buffer might contain information based on the node’s position and transform.

## See Also

### Constants
- [SCNBufferFrequency.perFrame](./perframe.md)
  Execute the binding handler once for each frame to be rendered using the shader.
- [SCNBufferFrequency.perShadable](./pershadable.md)
  Execute the binding handler once for each frame, for each node, for each material or geometry to be rendered using the shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbufferfrequency/pernode)*