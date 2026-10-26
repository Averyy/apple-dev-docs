# setScissorRects:count:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets an array of scissor rectangles for a fragment scissor test.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) setScissorRects:(const MTLScissorRect[]) scissorRects count:(NSUInteger) count;
```

#### Discussion

Metal uses the specific scissor rectangle corresponding to the index you specify via the `[[ viewport_array_index ]]` output attribute of the vertex shader function in the Metal Shading Language, discarding all fragments outside of the scissor rect.

## Parameters

- `scissorRects`: Array of [`MTLScissorRect`](../mtlscissorrect.md) structures.
- `count`: Number of [`MTLScissorRect`](../mtlscissorrect.md) structures in the array.

## See Also

### Configuring viewport and scissor behavior
- [func setViewport(MTLViewport)](./setviewport%28_%29.md)
  Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.
- [- setViewports:count:](./setviewports_count_.md)
  Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.
- [func setScissorRect(MTLScissorRect)](./setscissorrect%28_%29.md)
  Sets a scissor rectangle to discard fragments outside a specific area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setscissorrects:count:)*