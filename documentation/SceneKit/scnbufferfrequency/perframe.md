# SCNBufferFrequency.perFrame

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

Execute the binding handler once for each frame to be rendered using the shader.

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
case perFrame
```

```c
SCNBufferFrequencyPerFrame
```

## Discussion

Use this option when the contents of the buffer should be uniform across all uses of the shader when rendering a single frame, no matter how many different nodes, geometries, and materials use the shader program.

## See Also

### Constants
- [SCNBufferFrequency.perNode](./pernode.md)
  Execute the binding handler once for each frame, for each node to be rendered using the shader.
- [SCNBufferFrequency.perShadable](./pershadable.md)
  Execute the binding handler once for each frame, for each node, for each material or geometry to be rendered using the shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbufferfrequency/perframe)*