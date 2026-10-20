# SCNBufferFrequency.perShadable

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

Execute the binding handler once for each frame, for each node, for each material or geometry to be rendered using the shader.

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
case perShadable
```

```c
SCNBufferFrequencyPerShadable
```

#### Discussion

Use this option when the contents of the buffer should be specific to each geometry or material whose program property is set to this shader. For example, a material-specific buffer might contain information to be used in animating a texture.

## See Also

### Constants
- [SCNBufferFrequency.perFrame](./perframe.md)
  Execute the binding handler once for each frame to be rendered using the shader.
- [SCNBufferFrequency.perNode](./pernode.md)
  Execute the binding handler once for each frame, for each node to be rendered using the shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbufferfrequency/pershadable)*