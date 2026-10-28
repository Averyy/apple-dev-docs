# setViewports(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setViewports(_ viewports: [MTLViewport])
```

## Discussion

Metal clips fragments that lie outside of the viewport, and optionally clamps fragments outside of z-near/z-far range, depending on the value you assign to [`setDepthClipMode(_:)`](./setdepthclipmode%28_%29.md).

Metal selects the viewport to use from the `[[ viewport_array_index ]]` attribute you specify in the pipeline state’s vertex shader function in the Metal Shading Language.

## Parameters

- `viewports`: A Swift array of [`MTLViewport`](../mtlviewport.md) elements.

## See Also

### Configuring viewport and scissor behavior
- [func setViewport(MTLViewport)](./setviewport%28_%29.md)
  Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.
- [func setScissorRect(MTLScissorRect)](./setscissorrect%28_%29.md)
  Sets a scissor rectangle to discard fragments outside a specific area.
- [func setScissorRects([MTLScissorRect])](./setscissorrects%28_%29.md)
  Sets an array of scissor rectangles for a fragment scissor test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setviewports(_:))*