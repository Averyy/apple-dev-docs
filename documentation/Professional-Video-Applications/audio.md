# audio

**Framework**: Professional-Video-Applications  
**Role**: Article

References audio data from an `asset` or `effect` element.

## Overview

Attributes of an `audio` element:

| Attribute | Description |
| --- | --- |
| `srcID` | References the specific audio source (or track) in the asset. The default is `1`. |
| `role` | Assigns a role to the audio media component. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) Format is `main-role.subrole`. |
| `srcCh` | Identifies specific audio source channels in the asset. Value is a comma-separated series of 1-based channel indices. |
| `outCh` | Specifies output channels to send the audio. Value is a comma-separated series of channel tags: `L`, `R`, `C`, `LFE`, `Ls`, `Rs`, and `X`. |

For information on how to define audio components for story elements, see Audio Component Configuration for more information.

## See Also

### Story Elements
- [clip](./clip.md)
  Represents a basic unit of editing.
- [asset-clip](./asset-clip.md)
  References a single media asset.
- [sync-clip](./sync-clip.md)
  Contains a clip with its contained and anchored items synchronized.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/audio)*