# adjust-reorient

**Framework**: Professional-Video-Applications  
**Role**: Article

Reorients a spherical clip within a 360 project. 

## Overview

This element changes the direction in which the camera points. The element also assists leveling the horizon of the clip.

Attributes of the `adjust-reorient` element:

| Attribute | Description |
| --- | --- |
| `enabled` | Enables (`1`, default) or disables (`0`) this orientation adjustment. |
| `tilt` | The amount, in degrees, of tilt. A positive value tilts the camera down, and a negative value tilts the camera up. |
| `pan` | The amount, in degrees, of pan. A positive value pans the camera right, and a negative value pans the camera left. |
| `roll` | The amount, in degrees, of roll. A positive value rolls the camera clockwise, and a negative value rolls the camera counter clockwise. |
| `convergence` | A positive integer that moves the left and right eye images relative to each other. A positive value moves them farther apart and a negative value moves them closer together. |

## See Also

### 360 Adjustment Elements
- [adjust-360-transform](./adjust-360-transform.md)
  Specifies where to position a non-360 clip in a 360 project’s sphere.
- [adjust-orientation](./adjust-orientation.md)
  Specifies what part of a spherical clip to use in a non-360 project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/adjust-reorient)*