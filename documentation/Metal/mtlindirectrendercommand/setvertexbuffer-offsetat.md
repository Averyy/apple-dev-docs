# setVertexBuffer(_:offset:at:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets a vertex buffer argument for the command.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func setVertexBuffer(_ buffer: any MTLBuffer, offset: Int, at index: Int)
```

#### Discussion

If you created the indirect command buffer with [`inheritBuffers`](mtlindirectcommandbufferdescriptor/inheritbuffers.md) set to [`true`](https://developer.apple.com/documentation/swift/true), do not call this method. The command gets the arguments from the parent encoder when you execute the command.

If you need to pass other kinds of parameters to your shader, such as textures and samplers, create an argument buffer and pass it to the shader using this method.

## Parameters

- `buffer`: The buffer to set in the buffer argument table.
- `offset`: The location, in bytes relative to start of  ,   of the first byte of data for the vertex shader.
- `index`: An index in the buffer argument table. The maximum index is determined when you created the indirect command buffer.

## See Also

- [func setRenderPipelineState(any MTLRenderPipelineState)](mtlindirectrendercommand/setrenderpipelinestate(_:).md)
  Sets the render pipeline state object used by the command.
- [func setFragmentBuffer(any MTLBuffer, offset: Int, at: Int)](mtlindirectrendercommand/setfragmentbuffer(_:offset:at:).md)
  Sets a fragment buffer argument for the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectrendercommand/setvertexbuffer(_:offset:at:))*