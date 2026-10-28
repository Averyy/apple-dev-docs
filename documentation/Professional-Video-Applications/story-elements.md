# Story Elements

**Framework**: Professional-Video-Applications

Describe Final Cut Pro events and project data and their associated effects.

## Overview

Use Story Elements to arrange video or audio materials and titles or generators into a timeline, in the order you want them to appear when it plays on the timeline. Use the [Timing Attributes](./timing-attributes.md) for additional control over their precise timing.

Anchor one or more other story elements to each story element. An anchored item has a positive or negative lane index that either positions the item above or below its base element in the timeline.

For video elements, lane order also implies compositing order — items with higher lane indexes composite over elements with lower lane indexes. For audio elements, lane order doesn’t affect compositing. Items that reside inside, rather than above or below, a container are called contained items and have an implied lane index of zero.

Many story elements can contain annotations (keyword, markers, and so on) over a range of time, specified with the start and duration attributes. Add annotations  to story elements using the elements listed under Annotation and Note Elements. 

## Topics

### Story Elements
- [clip](./clip.md)
  Represents a basic unit of editing.
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
### Timeline Characteristics
- [Timeline Attributes](./timeline-attributes.md)
  Define characteristics of a timeline.
- [Timing Attributes](./timing-attributes.md)
  Schedule the element and its contained or anchored items in a timeline.
- [timeMap](./timemap.md)
  Adjust or retime the playback speed of an element.
- [conform-rate](./conform-rate.md)
  Apply rate conforming to match media frame rate to timeline frame rate.
- [Frame Sampling](./frame-sampling.md)
  Adjust the clip’s frame rate to match the project’s frame rate.
### Adjustment and Effects Elements
- [Adjustment Elements](./adjustment-elements.md)
  Alter the audio and video output of story elements by using adjustment elements.
- [transition](./transition.md)
  Applies transition effects that either stand by itself (no neighboring elements), combine two neighboring elements, or apply to a single element.
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
### Audio Component Configuration
- [audio-channel-source](./audio-channel-source.md)
  Defines an audio component by its source channels.
- [audio-role-source](./audio-role-source.md)
  Defines an audio component by its role.
- [mute](./mute.md)
  Suppresses audio output for the audio component over a range of time.
### Annotation and Note Elements
- [keyword](./keyword.md)
  An annotation that applies a keyword to a range of time.
- [marker](./marker.md)
  An annotation, with an optional to-do flag, that applies a text marker to a range of time.
- [chapter-marker](./chapter-marker.md)
  An annotation that applies to a range of time and indicates a chapter.
- [analysis-marker](./analysis-marker.md)
  An annotation that indicates the result of scene analysis to determine the number of people present and the shot and stabilization types.
- [rating](./rating.md)
  A rating annotation, such as favorite or reject, that applies to a range of time.
- [note](./note.md)
  Define descriptive notes that appliy to an entire element.
### Media Component Roles
- [Roles Attribute](./roles-attribute.md)
  Assign video, audio, title, and caption elements a role.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/story-elements)*