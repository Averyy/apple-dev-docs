# setScissorRects(_:)

**Framework**: Metal  
**Kind**: method

Configures multiple rectangles for the fragment scissor test.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst ?+
- macOS 10.13+
- tvOS 14.5+
- visionOS ?+

## Declaration

```swift
func setScissorRects(_ scissorRects: [MTLScissorRect])
```

## Mentions

- [Rendering to multiple viewports in a draw command](rendering-to-multiple-viewports-in-a-draw-command.md)

#### Discussion

The rendering pipeline discards any fragments that lie outside the scissor rectangle. The default scissor rectangle is the same size as the current render attachment, with its origin coordinates in the upper-left corner at `(0, 0)`.

Use this method to configure a different scissor rectangle for multiple viewports you configure with the [`setViewports(_:)`](mtlrendercommandencoder/setviewports(_:).md) method. Multiple viewports give your app the ability to draw into separate areas of an image with a single draw call. You can either set a single scissor rectangle for all viewports with the [`setScissorRect(_:)`](mtlrendercommandencoder/setscissorrect(_:).md) method, or set each viewport’s rectangle with this method.

> ❗ **Important**:  The number of scissor rectangles you pass to this method needs to match the number of viewports you configure with the [`setViewports(_:)`](mtlrendercommandencoder/setviewports(_:).md) method.

The maximum number of viewports and scissor rectangles a GPU supports varies by device family. For more information, see [`MTLGPUFamily`](mtlgpufamily.md) and [`Detecting GPU features and Metal software versions`](detecting-gpu-features-and-metal-software-versions.md).

The rendering pipeline sends each primitive to a single viewport and its associated scissor rectangle. You can select which viewport each primitive uses in your vertex shader by adding the `[[viewport_array_index]]` attribute to an output value.

> **Note**:  You can change the render pass’s scissor rectangle configuration by calling this method again or by calling the [`setScissorRect(_:)`](mtlrendercommandencoder/setscissorrect(_:).md) method.

The [`setScissorRect(_:)`](mtlrendercommandencoder/setscissorrect(_:).md) method is equivalent to calling this method with a single element in the `scissorRects` array.

## Parameters

- `scissorRects`: An array of   instances the command applies to the render pipeline for clipping.

## See Also

- [func setViewport(MTLViewport)](mtlrendercommandencoder/setviewport(_:).md)
  Configures the render pipeline with a viewport that applies a transformation and a clipping rectangle.
- [func setViewports([MTLViewport])](mtlrendercommandencoder/setviewports(_:).md)
  Configures the render pipeline with multiple viewports that apply transformations and clipping rectangles.
- [func setScissorRect(MTLScissorRect)](mtlrendercommandencoder/setscissorrect(_:).md)
  Configures a rectangle for the fragment scissor test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setscissorrects(_:))*