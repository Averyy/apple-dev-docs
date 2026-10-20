# setScissorRect(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets a scissor rectangle to discard fragments outside a specific area.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setScissorRect(_ rect: MTLScissorRect)
```

```objc
- (void) setScissorRect:(MTLScissorRect) rect;
```

#### Discussion

Metal performs a scissor test and discards all fragments outside of the scissor rect.

## Parameters

- `rect`: [`MTLScissorRect`](../mtlscissorrect.md) rectangle to specify. This rectangle needs to lie completely within the current render attachment.

## See Also

### Configuring viewport and scissor behavior
- [func setViewport(MTLViewport)](./setviewport%28_%29.md)
  Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.
- [func setViewports([MTLViewport])](./setviewports%28_%29.md)
  Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.
- [func setScissorRects([MTLScissorRect])](./setscissorrects%28_%29.md)
  Sets an array of scissor rectangles for a fragment scissor test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setscissorrect(_:))*