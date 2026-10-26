# text

**Framework**: Professional-Video-Applications  
**Role**: Article

Describes a block of text that appears in a title or caption on a timeline.

#### Overview

You can have one or more text blocks in a title or caption.

A text block can have different text styles. Use the `text-style` and `text-style-def` elements to describe the text style for each portion. Use the [Text Element Caption Attributes](./text.md#Text-Element-Caption-Attributes) when describing a caption text block.

> **Note**:  FCPXML 1.8 and later includes support to describie caption and subtitles.

##### Text Element Caption Attributes

| Element | Description |
| --- | --- |
| `display-style` | Specifies how a text block in a CEA-608 caption appears during playback. Valid values are: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `pop-on` — Displays all text at once. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `paint-on` — Displays text one character at a time as if it’s being written in real-time. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `roll-up` — Displays one line of text at a time, and new lines roll up from the bottom. |
| `roll-up-height` | Specifies the number of lines to use for the roll-up animation. |
| `position` | Specifies the relative position of a text block in a CEA-608 caption in the video frame, for example “`4 1`”. |
| `placement` | Specifies the relative position of an ITT (iTunes Timed Text) subtitle text block in the video frame. Valid values are: `top`, `bottom`, `left`, and `right`. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) **Note**: This attribute is ignored for a SRT (SubRip Text) caption text block. |
| `alignment` | Specifies the relative position of a text block in a CEA-608 caption in the video frame. Valid values are: `left`, `center`, and `right`. |

## See Also

### Text and Style Elements
- [text-style](./text-style.md)
  Describes text style for a segment of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/text)*