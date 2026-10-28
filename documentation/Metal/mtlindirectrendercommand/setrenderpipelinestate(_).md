# setRenderPipelineState(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the render pipeline state for the command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setRenderPipelineState(_ pipelineState: any MTLRenderPipelineState)
```

```objc
- (void) setRenderPipelineState:(id<MTLRenderPipelineState>) pipelineState;
```

## Discussion

You don’t need to call this method if you create an indirect command buffer with its [`inheritPipelineState`](../mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) property equal to [`true`](../../Swift/true.md). The command gets the pipeline state from the parent encoder when it runs.

If you created the indirect command buffer with [`inheritPipelineState`](../mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) set to [`false`](../../Swift/false.md), you need to set the pipeline state prior to encoding the drawing command.

## Parameters

- `pipelineState`: The rendering pipeline state object to use.

## See Also

### Setting command arguments
- [func setVertexBuffer(any MTLBuffer, offset: Int, at: Int)](./setvertexbuffer%28_,offset,at%29.md)
  Sets a vertex buffer argument for the command.
- [func setFragmentBuffer(any MTLBuffer, offset: Int, at: Int)](./setfragmentbuffer%28_,offset,at%29.md)
  Sets a fragment buffer argument for the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectrendercommand/setrenderpipelinestate(_:))*