# setRenderPipelineState(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets the render pipeline state object used by the command.

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

#### Discussion

If you created the indirect command buffer with [`inheritPipelineState`](mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) set to [`true`](https://developer.apple.com/documentation/swift/true), do not call this method. The command gets the pipeline state object from the parent encoder when you execute the command.

If you created the indirect command buffer with [`inheritPipelineState`](mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) set to [`false`](https://developer.apple.com/documentation/swift/false), you must set the pipeline state prior to encoding the drawing command.

## Parameters

- `pipelineState`: The rendering pipeline state object to use.

## See Also

- [func setVertexBuffer(any MTLBuffer, offset: Int, at: Int)](mtlindirectrendercommand/setvertexbuffer(_:offset:at:).md)
  Sets a vertex buffer argument for the command.
- [func setFragmentBuffer(any MTLBuffer, offset: Int, at: Int)](mtlindirectrendercommand/setfragmentbuffer(_:offset:at:).md)
  Sets a fragment buffer argument for the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectrendercommand/setrenderpipelinestate(_:))*