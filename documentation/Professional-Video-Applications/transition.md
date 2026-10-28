# transition

**Framework**: Professional-Video-Applications  
**Role**: Article

Applies transition effects that either stand by itself (no neighboring elements), combine two neighboring elements, or apply to a single element.

## Overview

Transition effect applies to elements contained in a `spine` or `mc-angle`. Use the `offset` and `duration` attributes to define the position and extent of the transition effect. The [filter-video](./filter-video.md) and [filter-audio](./filter-audio.md) elements specify the effect to apply. 

> **Note**:  When an audio filter specifies an audio cross fade, the cross fade doesn’t take effect on either side when the clip has audio-specific timing set by the `audioStart` or `audioDuration` attributes. This is known as a J- or L-cut, depending on the side of the transition on which it it occurs.

## See Also

### Adjustment and Effects Elements
- [Adjustment Elements](./adjustment-elements.md)
  Alter the audio and video output of story elements by using adjustment elements.
- [title](./title.md)
  Represents a title with one or more text blocks.
- [caption](./caption.md)
  Represents a closed-caption or subtitle with one or more text blocks.
- [filter-audio](./filter-audio.md)
  A filter element that references an audio effect.
- [filter-video](./filter-video.md)
  A filter element that references a video effect.
- [Masked Filters](./masked-filters.md)
  Designate a region to which you apply video filter by using a collection of masks.
- [Adjustment Attributes and Effect Parameters](./adjustment-attributes-and-effect-parameters.md)
  Specify values to change adjustment attributes and effects parameters.
- [Animation](./animation.md)
  Create animations by changing specific adjustment attributes and effect parameters over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/transition)*