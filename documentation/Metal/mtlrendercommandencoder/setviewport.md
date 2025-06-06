# setViewport(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the render pipeline with a viewport that applies a transformation and a clipping rectangle.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setViewport(_ viewport: MTLViewport)
```

#### Discussion

The render pipeline linearly maps vertex positions from normalized device coordinates to viewport coordinates by applying a viewport during the rasterization stage. It applies the transform first and then rasterizes the primitive while clipping any fragments outside the scissor rectangle (see [`setScissorRect(_:)`](mtlrendercommandencoder/setscissorrect(_:).md)) or the render target’s extents.

The viewport’s [`originX`](mtlviewport/originx.md) and [`originY`](mtlviewport/originy.md) properties, which default to `0.0`, represent the number of pixels from the top-left corner of the render target. Positive [`originX`](mtlviewport/originx.md) values go to the right and positive [`originY`](mtlviewport/originy.md) values go downward. The default values for its [`width`](mtlviewport/width.md) and [`height`](mtlviewport/height.md) properties are the render target’s width and height, respectively. The default values for its [`znear`](mtlviewport/znear.md) and [`zfar`](mtlviewport/zfar.md) properties are `0.0` and `1.0`, respectively, which you can flip.

> **Note**:  You can change the render pass’s viewport configuration by calling this method again, or by calling the [`setViewports(_:)`](mtlrendercommandencoder/setviewports(_:).md) method.

 You can change the render pass’s viewport configuration by calling this method again, or by calling the [`setViewports(_:)`](mtlrendercommandencoder/setviewports(_:).md) method.

## Parameters

- `viewport`: An   instance the command applies to the render pipeline for transformations and clipping.

## See Also

- [func setViewports([MTLViewport])](mtlrendercommandencoder/setviewports(_:).md)
  Configures the render pipeline with multiple viewports that apply transformations and clipping rectangles.
- [func setScissorRect(MTLScissorRect)](mtlrendercommandencoder/setscissorrect(_:).md)
  Configures a rectangle for the fragment scissor test.
- [func setScissorRects([MTLScissorRect])](mtlrendercommandencoder/setscissorrects(_:).md)
  Configures multiple rectangles for the fragment scissor test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setviewport(_:))*