# Rendering in FxPlug

**Framework**: Professional-Video-Applications  
**Role**: Article

Use Metal or other frameworks to render images with your FxPlug plug-in.

## Overview

[`FxImageTile`](../professional_video_applications/fximagetile.md) is a new class for FxPlug 4 that combines and improves the frame information previously found in `FxRenderInfo` and `FxImage`, including bounds, pixel transforms, field and field order, and the image’s origin. Incoming images are now presented as an [IOSurface](../IOSurface/IOSurface.md), which is one of the biggest changes to FxPlug 4.

Rendering always involves these four steps:

1. Gather the state your plug-in needs to render by checking parameter values and making calculations. [Communicating with the plug-in state](./communicating-with-the-plug-in-state.md) explains how to prepare required information for you plug-in to render.
2. Tell the host application what the output area will be, given the input area. See [Set the destination rectangle bounds](./working-with-tiled-images.md#Set-the-destination-rectangle-bounds).
3. For each tile of the output the host requests, tell it which tile of the inputs you need to render. [Working with tiled images](./working-with-tiled-images.md) explains how to set input and output bounds.
4. Draw each output tile. See [`renderDestinationImage(_:sourceImages:pluginState:at:)`](../professional_video_applications/fxtileableeffect/renderdestinationimage%28_,sourceimages,pluginstate,at%29.md).

When rendering, your plug-in will be given an [`FxImageTile`](../professional_video_applications/fximagetile.md) for output. Use this to return a texture to the host application when your plug-in has finished rendering. The `outputImage` contains a [`deviceRegistryID`](../professional_video_applications/fximagetile/deviceregistryid.md), which identifies what graphics card the texture is on. This is a read-only property.

For an example of how to work with [`deviceRegistryID`](../professional_video_applications/fximagetile/deviceregistryid.md), see the `FxDynamicRegistration` example. Specifically, look at `PAEMTLBrightnessRenderer.m`, in `renderWithBrightness` where the `OutputTexture` uses the `OutputImag`e’s `deviceRegistryID` value to create Metal state, and Input and Output textures.

> **Note**:  Your plug-in may suffer from a performance hit if you set [`kIOSurfacePixelSizeCastingAllowed`](../IOSurface/kiosurfacepixelsizecastingallowed.md) on your IOSurface, so its use is generally *not* recommended. You set this flag to ensure that pixel locations are kept in order in VRAM, and then you can use custom pixel packing in your plug-in. If you do need this flag, when converting from 4:4:4 to 4:2:2 formats for example, the host app will provide a copy of the input and output IOSurface, so you can unpack your specific pixel format in the plug-in, and likewise pack your specific pixel format into the output [IOSurface](../IOSurface/IOSurface.md).

## See Also

### Rendering
- [Communicating with the plug-in state](./communicating-with-the-plug-in-state.md)
  Prepare the necessary information, such as parameter values, for your FxPlug plug-in to render.
- [Working with tiled images](./working-with-tiled-images.md)
  Render only the necessary tiles of an image in your FxPlug plug-in to improve efficiency.
- [Optimizing FxPlug plug-ins](./optimizing-fxplug-plug-ins.md)
  Maintain consistent rendering at all resolutions and aspect ratios by using pixel transforms.
- [protocol FxTileableEffect](../professional_video_applications/fxtileableeffect.md)
  The designated initializer for your plug-in for rendering only certain portions of the plug-in’s output, referred to as tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/rendering-in-fxplug)*