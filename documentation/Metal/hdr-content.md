# HDR content

**Framework**: Metal

Take advantage of high dynamic range to present more vibrant colors in your apps and games.

#### Overview

High dynamic range (HDR) content has a wider range of brightness levels than standard definition content. Certain displays, which macOS refers to as extended dynamic range (EDR) displays, can physically replicate those extra brightness values on a screen. You can use Metal to detect EDR displays and work with HDR content, such as from a video asset or directly from your app.

## Topics

### High dynamic range content
- [Processing HDR images with Metal](processing-hdr-images-with-metal.md)
  Implement a post-processing pipeline using the latest features on Apple GPUs.
- [Displaying HDR content in a Metal layer](displaying-hdr-content-in-a-metal-layer.md)
  Bring your high dynamic range (HDR) content to compatible Mac displays.
- [Determining support for EDR values](determining-support-for-edr-values.md)
  Check whether a display supports EDR.
- [Using color spaces to display HDR content](using-color-spaces-to-display-hdr-content.md)
  Use a color space when you don’t need to edit or process the pixel data.
- [Using system tone mapping on video content](using-system-tone-mapping-on-video-content.md)
  Use EDR metadata to apply the default system tone mapping to a layer.
- [Performing your own tone mapping](performing-your-own-tone-mapping.md)
  Apply your own tone mapping to get the exact behavior you want.
- [Implementing tone mapping on reference displays](implementing-tone-mapping-on-reference-displays.md)
  Detect reference displays and keep your content within the capabilities of the display hardware.

## See Also

- [Managing your game window for Metal in macOS](managing-your-game-window-for-metal-in-macos.md)
  Set up a window and view for optimally displaying your Metal content.
- [Managing your Metal app window in iPadOS](managing-your-metal-app-window-in-ipados.md)
  Set up a window that handles dynamically resizing your Metal content.
- [Adapting your game interface for smaller screens](adapting-your-game-interface-for-smaller-screens.md)
  Make text legible on all devices the player chooses to run your game on.
- [Onscreen presentation](onscreen-presentation.md)
  Show the output from a GPU’s rendering pass to the user in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/hdr-content)*