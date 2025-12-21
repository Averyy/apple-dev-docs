# Using color spaces to display HDR content

**Framework**: Metal

Use a color space when you don’t need to edit or process the pixel data.

#### Overview

If you aren’t editing the content in a linear color space, and simply need to display the content with the correct transfer function, use a color space that includes that transfer function. Create a Metal layer and set its [`wantsExtendedDynamicRangeContent`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer/wantsExtendedDynamicRangeContent) property to [`true`](https://developer.apple.com/documentation/Swift/true). Set the color space that matches the color primaries and transfer function of your content. The code below creates a Metal layer for content in the BT.2020 color space using the PQ transfer function:

## See Also

- [Processing HDR images with Metal](processing-hdr-images-with-metal.md)
  Implement a post-processing pipeline using the latest features on Apple GPUs.
- [Displaying HDR content in a Metal layer](displaying-hdr-content-in-a-metal-layer.md)
  Bring your high dynamic range (HDR) content to compatible Mac displays.
- [Determining support for EDR values](determining-support-for-edr-values.md)
  Check whether a display supports EDR.
- [Using system tone mapping on video content](using-system-tone-mapping-on-video-content.md)
  Use EDR metadata to apply the default system tone mapping to a layer.
- [Performing your own tone mapping](performing-your-own-tone-mapping.md)
  Apply your own tone mapping to get the exact behavior you want.
- [Implementing tone mapping on reference displays](implementing-tone-mapping-on-reference-displays.md)
  Detect reference displays and keep your content within the capabilities of the display hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/using-color-spaces-to-display-hdr-content)*