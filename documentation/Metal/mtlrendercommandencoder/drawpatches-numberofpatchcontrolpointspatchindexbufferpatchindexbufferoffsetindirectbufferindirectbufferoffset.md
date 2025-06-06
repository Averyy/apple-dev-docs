# drawPatches(numberOfPatchControlPoints:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders multiple instances of tessellated patches with indirect arguments.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func drawPatches(numberOfPatchControlPoints: Int, patchIndexBuffer: (any MTLBuffer)?, patchIndexBufferOffset: Int, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)
```

#### Discussion

Indirect drawing methods may help your app avoid expensive latency costs. This is because the command reads arguments from an [`MTLBuffer`](mtlbuffer.md) instance instead of using the CPU to pass parameters to the command.

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [`MTLCommandBuffer`](mtlcommandbuffer.md).

## Parameters

- `numberOfPatchControlPoints`: The number of control points for each patch, which needs to be in the range  .
- `patchIndexBuffer`: An   instance that contains the indices to patches.
- `patchIndexBufferOffset`: An integer that represents the location, in bytes, from the start of   where the patch indices begin.
- `indirectBuffer`: An   instance with data that matches the layout of the   structure.
- `indirectBufferOffset`: See the   to check for offset alignment requirements for buffers in   and   address space.

## See Also

- [func drawPatches(numberOfPatchControlPoints: Int, patchStart: Int, patchCount: Int, patchIndexBuffer: (any MTLBuffer)?, patchIndexBufferOffset: Int, instanceCount: Int, baseInstance: Int)](mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints:patchstart:patchcount:patchindexbuffer:patchindexbufferoffset:instancecount:baseinstance:).md)
  Encodes a draw command that renders multiple instances of tessellated patches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints:patchindexbuffer:patchindexbufferoffset:indirectbuffer:indirectbufferoffset:))*