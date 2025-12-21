# setViewports(_:)

**Framework**: Metal  
**Kind**: method

Configures the render pipeline with multiple viewports that apply transformations and clipping rectangles.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst ?+
- macOS 10.13+
- tvOS 14.5+
- visionOS ?+

## Declaration

```swift
func setViewports(_ viewports: [MTLViewport])
```

## Mentions

- [Rendering to multiple viewports in a draw command](rendering-to-multiple-viewports-in-a-draw-command.md)

#### Discussion

Use this method to configure multiple active viewports and corresponding scissor rectangles. Multiple viewports give your app the ability to draw into separate areas of an image with a single draw call. You can either set a single scissor rectangle for all viewports with the [`setScissorRect(_:)`](mtlrendercommandencoder/setscissorrect(_:).md) method, or set each viewport’s rectangle with the [`setScissorRects(_:)`](mtlrendercommandencoder/setscissorrects(_:).md) method.

> ❗ **Important**:  The number of scissor rectangles you pass to [`setScissorRects(_:)`](mtlrendercommandencoder/setscissorrects(_:).md) needs to match the number of viewports you configure with this method.

The maximum number of viewports and scissor rectangles a GPU supports varies by device family. For more information, see [`MTLGPUFamily`](mtlgpufamily.md) and [`Detecting GPU features and Metal software versions`](detecting-gpu-features-and-metal-software-versions.md).

The rendering pipeline sends each primitive to a single viewport and its associated scissor rectangle. You can select which viewport each primitive uses in your vertex shader by adding the `[[viewport_array_index]]` attribute to an output value.

The render pipeline linearly maps vertex positions from normalized device coordinates to viewport coordinates by applying a viewport during the rasterization stage. It applies the transform first and then rasterizes the primitive while clipping any fragments outside the scissor rectangle (see [`setScissorRect(_:)`](mtlrendercommandencoder/setscissorrect(_:).md)) or the render target’s extents.

The viewport’s [`originX`](mtlviewport/originx.md) and [`originY`](mtlviewport/originy.md) properties, which default to `0.0`, represent the number of pixels from the top-left corner of the render target. Positive [`originX`](mtlviewport/originx.md) values go to the right and positive [`originY`](mtlviewport/originy.md) values go downward. The default values for its [`width`](mtlviewport/width.md) and [`height`](mtlviewport/height.md) properties are the render target’s width and height, respectively. The default values for its [`znear`](mtlviewport/znear.md) and [`zfar`](mtlviewport/zfar.md) properties are `0.0` and `1.0`, respectively, which you can flip.

> **Note**:  You can change the render pass’s viewport configuration by calling this method again or by calling the [`setViewport(_:)`](mtlrendercommandencoder/setviewport(_:).md) method.

The [`setViewport(_:)`](mtlrendercommandencoder/setviewport(_:).md) method is equivalent to calling this method with a single viewport element in the `viewports` array.

## Parameters

- `viewports`: An array of   instances the command applies to the render pipeline for transformations and clipping.

## See Also

- [func setViewport(MTLViewport)](mtlrendercommandencoder/setviewport(_:).md)
  Configures the render pipeline with a viewport that applies a transformation and a clipping rectangle.
- [func setScissorRect(MTLScissorRect)](mtlrendercommandencoder/setscissorrect(_:).md)
  Configures a rectangle for the fragment scissor test.
- [func setScissorRects([MTLScissorRect])](mtlrendercommandencoder/setscissorrects(_:).md)
  Configures multiple rectangles for the fragment scissor test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setviewports(_:))*