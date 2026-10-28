# timeMap

**Framework**: Professional-Video-Applications  
**Role**: Article

Adjust or retime the playback speed of an element.

## Overview

A time map is defined with the `timeMap` element, which contains one or more `timept` elements that specify the new timing. FInal Cut Pro adjusts the parent element’s playback speed over a range of time using points on a curve to interpolate values. For example, if the local time range for a clip is originally 0-5s, then the time map for playing this clip at 50 percent speed, followed by playback at -50 percent speed, might look like:

```swift
<timeMap>
    <timept time="0s" value="0s" interp="linear"/>
    <timept time="10s" value="5s" interp="linear"/>    <!-- In 0-10s, play the original 0-5s -->
    <timept time="20s" value="0s" interp="linear"/>    <!-- In 10-20s, play the original 5-0s -->
</timeMap>

```

A time map affects only an element’s own duration and the offsets of the element’s anchored items; it doesn’t modify the offsets of the element’s contained items (such as items with `lane=0`).

## See Also

### Timeline Characteristics
- [Timeline Attributes](./timeline-attributes.md)
  Define characteristics of a timeline.
- [Timing Attributes](./timing-attributes.md)
  Schedule the element and its contained or anchored items in a timeline.
- [conform-rate](./conform-rate.md)
  Apply rate conforming to match media frame rate to timeline frame rate.
- [Frame Sampling](./frame-sampling.md)
  Adjust the clip’s frame rate to match the project’s frame rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/timemap)*