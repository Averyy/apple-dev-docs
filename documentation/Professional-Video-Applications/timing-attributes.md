# Timing Attributes

**Framework**: Professional-Video-Applications  
**Role**: Article

Schedule the element and its contained or anchored items in a timeline.

## Overview

Typically, timing attribute values are a multiple of the frame duration for the respective timeline. Otherwise, Final Cut Pro inserts a gap to maintain the specified timing upon import. A warning message appears when this happens.

This table lists the time value attributes:

| Attribute | Description |
| --- | --- |
| `offset` | An element’s location in parent time, or base element’s time for an anchor. |
| `start` | The start of an element’s local timeline used to schedule its contained and anchored items. |
| `duration` | An element’s extent in parent time. |

The parent elements limt the time range for contained items. But, they don’t limit the time range for anchored items. However, an ancestor that either directly or indirectly contains the parent may limit anchored items.

Fina Cut Pro expresses time values as a rational number of seconds with a 64-bit numerator and a 32-bit denominator. Frame rates for NTSC-compatible media, for example, use a frame duration of 1001/30000s (29.97 fps) or 1001/60000s (59.94 fps). If a time value is equal to a whole number of seconds, Final Cut Pro may reduce the fraction into whole seconds (for example, 5s).

## See Also

### Timeline Characteristics
- [Timeline Attributes](./timeline-attributes.md)
  Define characteristics of a timeline.
- [timeMap](./timemap.md)
  Adjust or retime the playback speed of an element.
- [conform-rate](./conform-rate.md)
  Apply rate conforming to match media frame rate to timeline frame rate.
- [Frame Sampling](./frame-sampling.md)
  Adjust the clip’s frame rate to match the project’s frame rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/timing-attributes)*