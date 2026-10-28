# setFragmentBuffer(_:offset:at:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets a fragment buffer argument for the command.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func setFragmentBuffer(_ buffer: any MTLBuffer, offset: Int, at index: Int)
```

```objc
- (void) setFragmentBuffer:(id<MTLBuffer>) buffer offset:(NSUInteger) offset atIndex:(NSUInteger) index;
```

## Discussion

You don’t need to call this method if you create an indirect command buffer with its [`inheritBuffers`](../mtlindirectcommandbufferdescriptor/inheritbuffers.md) equal to [`true`](../../Swift/true.md). The command gets the arguments from the parent encoder when it runs.

If you need to pass other kinds of parameters to your shader, such as textures and samplers, create an argument buffer and pass it to the shader using this method.

## Parameters

- `buffer`: The buffer to set in the buffer argument table.
- `offset`: The location, in bytes relative to start of `buffer`, of the first byte of data for the fragment shader.
- `index`: An index in the buffer argument table. The maximum index is determined when you created the indirect command buffer.

## See Also

### Setting command arguments
- [func setRenderPipelineState(any MTLRenderPipelineState)](./setrenderpipelinestate%28_%29.md)
  Sets the render pipeline state for the command.
- [func setVertexBuffer(any MTLBuffer, offset: Int, at: Int)](./setvertexbuffer%28_,offset,at%29.md)
  Sets a vertex buffer argument for the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectrendercommand/setfragmentbuffer(_:offset:at:))*