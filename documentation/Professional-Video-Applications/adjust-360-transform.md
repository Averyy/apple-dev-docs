# adjust-360-transform

**Framework**: Professional-Video-Applications  
**Role**: Article

Specifies where to position a non-360 clip in a 360 project’s sphere.

## Overview

Attributes of `adjust-360-transform` element:

| Attribute | Description |
| --- | --- |
| `enabled` | Enables (`1`, default) or disables (`0`) this orientation adjustment. |
| `coordinates` | Specifies whether the position of the clip is in Cartesian coordinates or spherical coordinates. This attribute is required. |
| `latitude` | For spherical coordinates, the amount, in degrees, of tilt. A positive value tilts the position of the clip upward, and a negative value tilts downward. |
| `longitude` | For spherical coordinates, the amount, in degrees, of pan. A positive value pans the clip’s position to the left and a negative value pans to the right. |
| `distance` | Adjusts the distance between the non-360 clip and the center of the project’s sphere. As the value increases, the non-360 clip moves farther from the center. |
| `xPosition`, `yPosition`, and `zPosition` | For Cartesian coordinates, the position of the clip relative to the sphere of the project timeline. |
| `xOrientation`, `yOrientation`, and `zOrientation` | The amount, in degrees, of tilt, pan, or roll of the clip at the position in the sphere of the project determined by the coordinate parameters. |
| `autoOrient` | A value of `1` (default) indicates the clip image is automatically oriented toward the view point. |
| `convergence` | For a stereoscopic 360 project, the value, between `-1.0` and `1.0`, moves the left and right eye projections relative to each other. |
| `interaxial` | Specifies the depth for a sterioscopic 360 project, a value, between `0` and `1.0`. |
| `scale` | A two-dimensional (`x y`) value that specifies the percentage amount to resize the clip in each dimension from its original frame size (for example, “25 25”). ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) The default is (1, 1). |

## See Also

### 360 Adjustment Elements
- [adjust-orientation](./adjust-orientation.md)
  Specifies what part of a spherical clip to use in a non-360 project.
- [adjust-reorient](./adjust-reorient.md)
  Reorients a spherical clip within a 360 project. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/adjust-360-transform)*