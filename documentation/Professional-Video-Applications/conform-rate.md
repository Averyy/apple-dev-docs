# conform-rate

**Framework**: Professional-Video-Applications  
**Role**: Article

Apply rate conforming to match media frame rate to timeline frame rate.

## Overview

When your media has specific combinations of timeline frame rate and media frame rate, Final Cut Pro automatically applies rate conforming by converting the media frame rate to match the timeline frame rate, as shown in the Final Cut Pro rate conforming chart below. As a result, Final Cut Pro also adjusts the duration. When this occurs, the Rate Conform section appears in Final Cut Pro Video Inspector. Use the `conform-rate` element to indicate rate conforming.

> **Note**:  In FCPXML 1.2, `timeMap` element was used to apply rate conforming with a `rateConform` attribute value of 1. Starting in FCPXML 1.3, use `conformRate` element to represent rate conforming.

How Final Cut Pro applies rate conforming between the media and timeline frame rates:

| Media Frame Rate | 23.98p | 24p | 25p, 25i, or 50p | 29.97p, 59.94p, or 29.97i | 30p or 60p |
| --- | --- | --- | --- | --- | --- |
| 23.98p | — | 24p | 25p | — | — |
| 24p | 23.98p | — | 25p | — | — |
| 25p | 23.98p | 24p | — | — | — |
| 29.97p | — | — | — | — | 30p |
| 30p | — | — | — | 29.97p | — |
| 50p | 47.96p | 48p | — | — | — |
| 59.94p | — | — | — | — | 60p |
| 60p | — | — | — | 59.94p | — |
| 25i | 47.96p | 48p | — | — | — |
| 29.97i | — | — | — | — | 60p |

## See Also

### Timeline Characteristics
- [Timeline Attributes](./timeline-attributes.md)
  Define characteristics of a timeline.
- [Timing Attributes](./timing-attributes.md)
  Schedule the element and its contained or anchored items in a timeline.
- [timeMap](./timemap.md)
  Adjust or retime the playback speed of an element.
- [Frame Sampling](./frame-sampling.md)
  Adjust the clip’s frame rate to match the project’s frame rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/conform-rate)*