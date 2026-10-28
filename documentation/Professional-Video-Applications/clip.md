# clip

**Framework**: Professional-Video-Applications  
**Role**: Article

Represents a basic unit of editing.

## Overview

Use a `clip` element to describe a timeline sequence created from a source media file. A `clip` contains `video` and/or `audio` elements, each of which represents a media component (usually a track) in media. Specify the timing of the edit through the [Timing Attributes](./timing-attributes.md).

You can also use a `clip` element as an immediate child element of an `event` element to represent a browser clip. In this case, use the [Timeline Attributes](./timeline-attributes.md) to specify its format, and so on.

## See Also

### Story Elements
- [asset-clip](./asset-clip.md)
  References a single media asset.
- [sync-clip](./sync-clip.md)
  Contains a clip with its contained and anchored items synchronized.
- [audio](./audio.md)
  References audio data from an `asset` or `effect` element.
- [video](./video.md)
  References  video data from an `asset` or `effect` element.
- [mc-clip](./mc-clip.md)
  References a multicam media.
- [ref-clip](./ref-clip.md)
  References a compound clip media.
- [gap](./gap.md)
  Defines a placeholder element that has no intrinsic audio or video data.
- [spine](./spine.md)
  Contains elements ordered sequentially in time.
- [audition](./audition.md)
  Contains one active story element followed by alternative story elements in the audition container.
- [sequence](./sequence.md)
  A container that represents the top-level sequence for a Final Cut Pro project or compound clip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/clip)*