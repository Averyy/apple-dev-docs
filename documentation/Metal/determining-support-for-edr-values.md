# Determining support for EDR values

**Framework**: Metal

Check whether a display supports EDR.

#### Overview

Discover whether a display supports EDR values by reading the [`maximumPotentialExtendedDynamicRangeColorComponentValue`](https://developer.apple.com/documentation/AppKit/NSScreen/maximumPotentialExtendedDynamicRangeColorComponentValue) property on an [`NSScreen`](https://developer.apple.com/documentation/AppKit/NSScreen) instance for that display. A value greater than `1.0` indicates that the display supports EDR values; otherwise, the display supports only SDR values.

This property’s value is independent of the current state of the display. It’s possible for a display to support EDR but to be unable to present those values right now. For information about the current state of the display, check the [`maximumExtendedDynamicRangeColorComponentValue`](https://developer.apple.com/documentation/AppKit/NSScreen/maximumExtendedDynamicRangeColorComponentValue) property.

## See Also

- [Processing HDR images with Metal](processing-hdr-images-with-metal.md)
  Implement a post-processing pipeline using the latest features on Apple GPUs.
- [Displaying HDR content in a Metal layer](displaying-hdr-content-in-a-metal-layer.md)
  Bring your high dynamic range (HDR) content to compatible Mac displays.
- [Using color spaces to display HDR content](using-color-spaces-to-display-hdr-content.md)
  Use a color space when you don’t need to edit or process the pixel data.
- [Using system tone mapping on video content](using-system-tone-mapping-on-video-content.md)
  Use EDR metadata to apply the default system tone mapping to a layer.
- [Performing your own tone mapping](performing-your-own-tone-mapping.md)
  Apply your own tone mapping to get the exact behavior you want.
- [Implementing tone mapping on reference displays](implementing-tone-mapping-on-reference-displays.md)
  Detect reference displays and keep your content within the capabilities of the display hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/determining-support-for-edr-values)*