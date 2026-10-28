# adjust-orientation

**Framework**: Professional-Video-Applications  
**Role**: Article

Specifies what part of a spherical clip to use in a non-360 project.

## Overview

Attributes of `adjust-orientation` element:

| Attribute | Description |
| --- | --- |
| `enabled` | Enables (`1`, default) or disables (`0`) this orientation adjustment. |
| `tilt` | The amount, in degrees, of tilt. A positive value tilts the view upward, and a negative value tilts downward. |
| `pan` | The amount, in degrees, of pan. A positive value pans the view to the left, and a negative value pans to the right. |
| `roll` | The amount, in degrees, of roll. A positive value rolls the view counter-clockwise, and a negative value rolls it clockwise. |
| `fieldOfView` | The horizontal field of view, measured in degrees. When the value increases, you see more of the spherical clip. |
| `mapping` | Set this attribute to `tinyPlanet` to project the entire sphere of a 360 clip through a `stereographic` projection within a normal project. Set to `normal` to show a portion of 360 image at a time. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) Valid values are : `normal` and `tinyPlanet`. |

## See Also

### 360 Adjustment Elements
- [adjust-360-transform](./adjust-360-transform.md)
  Specifies where to position a non-360 clip in a 360 project’s sphere.
- [adjust-reorient](./adjust-reorient.md)
  Reorients a spherical clip within a 360 project. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/adjust-orientation)*