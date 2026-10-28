# adjust-blend

**Framework**: Professional-Video-Applications  
**Role**: Article

Modifies the compositing blend mode and opacity percentage.

## Overview

To modify the compositing blend mode and opacity percentage in the ranage [0.0..1.0] of the visible image, use the following attributes:

| Attribute | Description |
| --- | --- |
| `amount` | A fractional value that specifies the opacity amount, for example, `0.75`. |
| `mode` | An integer value that corresponds to a built-in FCP blend mode; see [Blend Modes](./adjust-blend.md#Blend-Modes) for a list of supported values. |

### Blend Modes

- 0 (Normal)
- 2 (Subtract)
- 3 (Darken)
- 4 (Multiply)
- 5 (Color Burn)
- 6 (Linear Burn)
- 8 (Add)
- 9 (Lighten)
- 10 (Screen)
- 11 (Color Dodge)
- 12 (Linear Dodge)
- 14 (Overlay)
- 15 (Soft Light)
- 16 (Hard Light)
- 17 (Vivid Light)
- 18 (Linear Light)
- 19 (Pin Light)
- 20 (Hard Mix)
- 22 (Difference)
- 23 (Exclusion)
- 25 (Stencil Alpha)
- 26 (Stencil Luma)
- 27 (Silhouette Alpha)
- 28 (Silhouette Luma)
- 29 (Behind)
- 31 (Alpha Add)
- 32 (Premultiplied Mix)

> **Note**:  XML generators can omit the value in parentheses, and parsers scan for the numeric value only.

## See Also

### Video Adjustment Elements
- [adjust-cinematic](./adjust-cinematic.md)
  Describes the focus of Cinematic Video clips.
- [adjust-conform](./adjust-conform.md)
  Modifies the image size of a clip.
- [adjust-corners](./adjust-corners.md)
  Modifies the corners of a visible image.
- [adjust-crop](./adjust-crop.md)
  Modifies the visible image width and height.
- [adjust-rollingShutter](./adjust-rollingshutter.md)
  Specifies the rolling shutter reduction to apply to a clip.
- [adjust-stabilization](./adjust-stabilization.md)
  Specifies the stabilization to aplly to a clip.
- [adjust-transform](./adjust-transform.md)
  Modifies the visible image through resizing, moving, or rotating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/adjust-blend)*