# mask-isolation

**Framework**: Professional-Video-Applications  
**Role**: Article

Describes a color isolation mask.

## Overview

The `mask-isolation` element has a `data` element that contains the information that describes the mask. The attributes below control the characteristics of the mask. You can give additional mask parameters using the `param` element.

| Attribute | Description |
| --- | --- |
| `type` | Determines the type of the isolation mask. The valid values are: `3D` or `HSL`. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) Default is `3D`.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) **Note**: The `type` attribute is new in FCPXML v1.9. |
| `blendMode` | Specifies how to combine the isolation mask with other masks for a masked filter.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) The valid values are: `add`, `subtract`, or `multiply` ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) Default is `multiply`. |

## See Also

### Mask Elements
- [mask-shape](./mask-shape.md)
  Describes a shape that serves as a mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/mask-isolation)*