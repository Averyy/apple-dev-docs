# setScissorRects(_:)

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

```swift
func setScissorRects(_ scissorRects: [MTLScissorRect])
```

## Discussion

Metal uses the specific scissor rectangle corresponding to the index you specify via the `[[ viewport_array_index ]]` output attribute of the vertex shader function in the Metal Shading Language, discarding all fragments outside of the scissor rect.

## Parameters

- `scissorRects`: A Swift array of [`MTLScissorRect`](../mtlscissorrect.md) elements.

## See Also

### Configuring viewport and scissor behavior
- [func setViewport(MTLViewport)](./setviewport%28_%29.md)
  Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.
- [func setViewports([MTLViewport])](./setviewports%28_%29.md)
  Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.
- [func setScissorRect(MTLScissorRect)](./setscissorrect%28_%29.md)
  Sets a scissor rectangle to discard fragments outside a specific area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setscissorrects(_:))*