# Implementing tone mapping on reference displays

**Framework**: Metal

Detect reference displays and keep your content within the capabilities of the display hardware.

#### Overview

Reference displays are calibrated to produce accurate brightness and color values within a specified range, which you use in a controlled environment to create optimized video content. Always establish if you’re using a reference display before you process any data so you can avoid system tone mapping and clamp pixel values to the range the display can accurately produce.

To determine if you’re using a reference display, read the screen’s [`maximumReferenceExtendedDynamicRangeColorComponentValue`](https://developer.apple.com/documentation/AppKit/NSScreen/maximumReferenceExtendedDynamicRangeColorComponentValue) property. If the display is a reference display, the value of this property is a nonzero value that represents the largest possible pixel value the display can reproduce without clamping or tone mapping. This value may be less than [`maximumExtendedDynamicRangeColorComponentValue`](https://developer.apple.com/documentation/AppKit/NSScreen/maximumExtendedDynamicRangeColorComponentValue).

To guarantee the reference display presents your content accurately, perform your own tone mapping in a linear color space and keep pixel values between `0.0` and the reference maximum. For more information, see [`Performing your own tone mapping`](performing-your-own-tone-mapping.md).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/implementing-tone-mapping-on-reference-displays)*