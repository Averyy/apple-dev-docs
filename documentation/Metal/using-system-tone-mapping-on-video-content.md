# Using system tone mapping on video content

**Framework**: Metal

Use EDR metadata to apply the default system tone mapping to a layer.

#### Overview

When processing video content, you usually want to work in a linear color space. You also want to display content that’s consistent with how playback would appear in AVFoundation or other playback mechanisms. To create content in your app that is consistent with the system behavior, create a Metal layer with a linear color space and attach an [`CAEDRMetadata`](https://developer.apple.com/documentation/QuartzCore/CAEDRMetadata) object defining how the system should tone map the video content.

The code below creates a Metal layer with an extended linear BT.2020 color space and metadata that applies an HDR10 tone mapping based on the reference display.

Your rendering code needs to generate pixel values consistent with the EDR metadata object. For example, in the above code, the `opticalOutputScale` was set to `100`, so a pixel value of `1.0` corresponds to `100` nits. For more information, see [`CAEDRMetadata`](https://developer.apple.com/documentation/QuartzCore/CAEDRMetadata).

## See Also

- [Processing HDR images with Metal](processing-hdr-images-with-metal.md)
  Implement a post-processing pipeline using the latest features on Apple GPUs.
- [Displaying HDR content in a Metal layer](displaying-hdr-content-in-a-metal-layer.md)
  Bring your high dynamic range (HDR) content to compatible Mac displays.
- [Determining support for EDR values](determining-support-for-edr-values.md)
  Check whether a display supports EDR.
- [Using color spaces to display HDR content](using-color-spaces-to-display-hdr-content.md)
  Use a color space when you don’t need to edit or process the pixel data.
- [Performing your own tone mapping](performing-your-own-tone-mapping.md)
  Apply your own tone mapping to get the exact behavior you want.
- [Implementing tone mapping on reference displays](implementing-tone-mapping-on-reference-displays.md)
  Detect reference displays and keep your content within the capabilities of the display hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/using-system-tone-mapping-on-video-content)*