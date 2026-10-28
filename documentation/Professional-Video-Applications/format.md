# format

**Framework**: Professional-Video-Applications

Reference a video-format definition.

## Overview

Use this element to reference one of the video formats listed under [Predefined Video Formats](./predefined-video-formats.md) through the `name` attribute, or use it to describe a custom video format using the [Format Element Attributes](./format.md#Format-Element-Attributes). For audio only assets, use the `FFFrameRateUndefined` format.

When `Format Element Attributes` exist, they override the predefined format value identified by the `name` attribute.

> **Note**:  In FCPXML 1.6 and earlier, Final Cut Pro ignores the `format` element attributes if you specify the name attribute.

### Format Element Attributes

| Attribute | Description |
| --- | --- |
| `frameDuration` | The frame duration as a time value. |
| `fieldOrder` | The field order for interlaced (`upper first` or `lower first`), or progressive video (`progressive`). |
| `width` | The video frame width, in pixels. |
| `height` | The video frame height, in pixels. |
| `paspH` | The relative width of a pixel when you encode video with non-square pixels. |
| `paspV` | The relative height of a pixel when you encode video with non-square pixels. |
| `colorSpace` | The asset’s color space. For information oh how to decribe a color space, see [Describing a Color Space](./format.md#Describing-a-Color-Space). |
| `projection` | The projection type to display a project or media. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) Valid values are: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `none` for a traditional project or media  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `equirectangular` or `cubic` for a 360 project or media ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `fisheye` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `back-to-back fisheye` |
| `stereoscopic` | The type of stereoscopic mode. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) The valide values are: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `mono`  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `side by side` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `over under` |

### Describing a Color Space

You can describe a color space in terms of its components (color primaries, transfer function, and YCbCr matrix). Color space enocdes each component as an integer value and combines it in a triplet with a hyphen (-) as the delimiter.  For example, 1-1-1 represents the standard Rec. 709 color profile, and 9-1-9 is the standard Rec. 2020 color profile in SDR with the traditional Rec. 709 transfer function. For more information on specific encoded values, see ISO/IEC 23001-8.

Use the color space triplets syntax to specify the `colorSpace` attribute of the `format` element and the `colorSpaceOverride` attribute of the `asset` element.

When Final Cut Pro exports FCPXML, it appends the name of the color space in parentheses to the triplet representation for well-known color spaces. For example 1-1-1 (Rec. 709) or 9-1-9 (Rec. 2020). On import, Final Cut Pro only uses the triplet and ignores the name within the parentheses.

The color space of a project or a multicam sequence can be one of those listed in [Well-Known Color Space Triplets](./asset.md#Well-Known-Color-Space-Triplets).

You cannot represemt still image color spaces in terms of components, so the triplet syntax isn’t valid. Instead, use one of the following values for the `colorSpaceOverride` attribute:

- `sRGB IEC61966-2.1`
- `Adobe RGB (1998`)

> **Note**:  FCPXML 1.7 added enhanced support for project and media color space and added support for HDR library processing mode.

## Topics

### Predefined Video Formats
- [Predefined Video Formats](./predefined-video-formats.md)
  Valid values for video formats.
### Resource Element Attributes
- [id](./id.md)
  Specifies a local identifier to use within the FCPXML document.
- [name](./name.md)
  Specifies the name of the resource.

## See Also

### Shared Resources and Reference Elements
- [asset](./asset.md)
  Define file-based media managed in a Final Cut Pro library.
- [media](./media.md)
  Describe a compound clip or a multi-camera media definition.
- [effect](./effect.md)
  Reference visual, audio, or custom effects.
- [locator](./locator.md)
  Describe a URL-based resource.
- [object-tracker](./object-tracker.md)
  Describe a tracked object such as a face or other moving object in a video clip.
- [tracking-shape](./tracking-shape.md)
  Define a shape that the object-tracker uses to match the movement of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/format)*