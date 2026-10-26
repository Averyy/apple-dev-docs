# asset-clip

**Framework**: Professional-Video-Applications  
**Role**: Article

References a single media asset.

#### Overview

Use an `asset-clip` element as a shorthand for a `clip` when it references the entire set of media components in a single media.

Specify the timing of the edit through the [Timing Attributes](./timing-attributes.md). The `start` and `duration` attributes of the `asset-clip` element apply to all media components in the asset.

Use the `audio-role` and `video-role` attributes to specify the main role. Generate subroles using the main role name, followed by a numerical suffix. For example, `dialogue.dialogue-1`, `dialogue.dialogue-2`, and so on.

Just as you do with the `clip` element, you can also use a `asset-clip` element as an immediate child element of an `event` element to represent a browser clip. In this case, use the [Timeline Attributes](./timeline-attributes.md) to specify its format, etc.

> **Note**:  FCPXML 1.6 added the `asset-clip` element to add both the audio and video media components from a media file as a clip.

## See Also

### Story Elements
- [clip](./clip.md)
  Represents a basic unit of editing.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/asset-clip)*