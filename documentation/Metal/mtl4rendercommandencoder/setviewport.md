# setViewport(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setViewport(_ viewport: MTLViewport)
```

#### Discussion

Metal clips fragments that lie outside this viewport, and optionally clamps fragments outside of z-near/z-far range depending on the value you assign to [`setDepthClipMode(_:)`](mtl4rendercommandencoder/setdepthclipmode(_:).md).

## Parameters

- `viewport`:   to set.

## See Also

- [func setViewports([MTLViewport])](mtl4rendercommandencoder/setviewports(_:).md)
  Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.
- [func setScissorRect(MTLScissorRect)](mtl4rendercommandencoder/setscissorrect(_:).md)
  Sets a scissor rectangle to discard fragments outside a specific area.
- [func setScissorRects([MTLScissorRect])](mtl4rendercommandencoder/setscissorrects(_:).md)
  Sets an array of scissor rectangles for a fragment scissor test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setviewport(_:))*