# adjust-transform

**Framework**: Professional-Video-Applications  
**Role**: Article

Modifies the visible image through resizing, moving, or rotating.

#### Overview

Modify the visible image using the following attributes:

| Attribute | Description |
| --- | --- |
| `enabled` | Enables (`1`, the default) or disables (`0`) this transform adjustment |
| `position` | A two-dimensional (xy) value that specifies the amount to move the frame in each dimension from its original location. These values are percentages based on the original frame height. For example, if the original frame height is 1,080 pixels, specifying `position=”10 10”` moves the frame 108 pixels to the right and 108 pixels up. |
| `scale` | A two-dimensional (xy) value that specifies the percentage amount to resize the frame in each dimension from its original frame size (for example, `25 25`). |
| `rotation` | The amount, in degrees, to rotate the frame. A positive value rotates counterclockwise and a negative value rotates clockwise, for example, `-180`. |
| `anchor` | A two-dimensional (xy) value that offsets the origin of the video image and its center of rotation. This value is expressed as a percentage of the scaled image height and defaults to `0 0`. |
| `tracking` | References a tracking shape associated with the transform adjustment. |

## See Also

### Video Adjustment Elements
- [adjust-blend](./adjust-blend.md)
  Modifies the compositing blend mode and opacity percentage.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/adjust-transform)*