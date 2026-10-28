# Timeline Attributes

**Framework**: Professional-Video-Applications  
**Role**: Article

Define characteristics of a timeline.

## Overview

The `sequence` element creates a new timeline. Use the timeline attributes to define its characteristics. Use the attributes with the `clip` element, when it appears as a top-level story element, to describe a browser clip in an event. The timeline attributes are:

| Attribute | Description |
| --- | --- |
| `format` | A reference to the video format defined by the `format` element. |
| `tcStart` | The timecode origin represented as a time value. See [Timing Attributes](./timing-attributes.md). |
| `tcFormat` | The timecode display format, either drop frame (`DF`) or nondrop frame (`NDF`, which is the default). |

### Timeline Audio Attributes

The `sequence` element can also contain the attributes in the table below, to define the audio characteristics of the new timeline:

| Attribute | Description |
| --- | --- |
| `audioLayout` | When you choose to render audio in a project timeline  to an export output, the `audioLayout` attribute defines the audio channels for each of the clips and audio components within the sequence. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) Valid values are `mono`, `stereo` (the default), or `surround`. Some  additional rules are: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For mono clips and audio components, the audio is split into two channels for a stereo layout, or assigned to the center channel if the layout is surround. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For stereo clips and audio components, the audio is mixed for a mono layout, or assigned to the left and right channels for surround. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) For surround clips and audio components, the audio is mixed down as appropriate for a stereo or mono layout. |
| `audioRate` | The audio sample rate. Valid values are  `2k`, `44.1k`, `48k`, `88k`, `96k`, `176.4k`, or `192k.` The default is `48k`. |

## See Also

### Timeline Characteristics
- [Timing Attributes](./timing-attributes.md)
  Schedule the element and its contained or anchored items in a timeline.
- [timeMap](./timemap.md)
  Adjust or retime the playback speed of an element.
- [conform-rate](./conform-rate.md)
  Apply rate conforming to match media frame rate to timeline frame rate.
- [Frame Sampling](./frame-sampling.md)
  Adjust the clip’s frame rate to match the project’s frame rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/timeline-attributes)*