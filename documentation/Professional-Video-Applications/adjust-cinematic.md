# adjust-cinematic

**Framework**: Professional-Video-Applications  
**Role**: Article

Describes the focus of Cinematic Video clips.

#### Overview

Cinematic Video clips are created when a user records in Cinematic mode using the Camera app on an iOS device. Use the `adjust-cinematic` element to modify the aperture of the cinematic effect and to reference associated cinematic data stored by Final Cut Pro.

| Attribute | Description |
| --- | --- |
| `enabled` | Enables (`1`, default) or disables (`0`) this cinematic adjustment. |
| `aperture` | Controls the depth of field of the cinematic effect. |
| `dataLocator` | References a locator resource used to store cinematic data from the iOS camera and any focus points the user has added. |

## See Also

### Video Adjustment Elements
- [adjust-blend](./adjust-blend.md)
  Modifies the compositing blend mode and opacity percentage.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/adjust-cinematic)*