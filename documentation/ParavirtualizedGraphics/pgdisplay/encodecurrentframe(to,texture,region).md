# encodeCurrentFrame(to:texture:region:)

**Framework**: Paravirtualized Graphics  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes Metal commands to process the current frame and write it to a texture.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
func encodeCurrentFrame(to commandBuffer: any MTLCommandBuffer, texture: any MTLTexture, region: MTLRegion) -> Bool
```

```objc
- (bool) encodeCurrentFrameToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer texture:(id<MTLTexture>) texture region:(MTLRegion) region;
```

## Return Value

Returns [`true`](../../Swift/true.md) if the method encoded the commands successfully; otherwise [`false`](../../Swift/false.md).

## Discussion

This method encodes Metal commands to process the new frame, dealing with color matching, gamma, and other factors. The GPU writes data to a region inside the destination texture, linearly scaled as necessary to fit in the specified region. The encoded commands won’t change any texture data outside the specified region.

The texture and command buffer must share the same Metal device object that you used to create the virtual graphics device. The destination texture must specify all of the usage bits that the display’s [`minimumTextureUsage`](./minimumtextureusage.md) property provides, but can specify additional flags.

Typically, you encode frame processing in response to a call to the frame event handler you specified when you created the display object. See [`newFrameEventHandler`](../pgdisplaydescriptor/newframeeventhandler.md) for more information.

## Parameters

- `commandBuffer`: The Metal command buffer for encoding the processing of the new frame.
- `texture`: The destination texture.
- `region`: The region within the Metal texture for the frame data to land in.

## See Also

### Handling Frame Updates
- [var guestPresentCount: Int](./guestpresentcount.md)
  The number of frame presents that the guest has generated since object creation.
- [var hostPresentCount: Int](./hostpresentcount.md)
  The number of unique frames that the host has encoded since object creation.
- [var minimumTextureUsage: MTLTextureUsage](./minimumtextureusage.md)
  The Metal texture usage flags necessary for any texture that can be a destination for frame data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay/encodecurrentframe(to:texture:region:))*