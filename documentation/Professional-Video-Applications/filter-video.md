# filter-video

**Framework**: Professional-Video-Applications  
**Role**: Article

A filter element that references a video effect.

## Overview

Apply video filters to elements that represent visual media, for example, `video`, `text`, `clip`, and `ref-clip` elements. For multicam clips, apply the video filters on the individual angles, represented by `mc-source` elements.

### Color Filters

Describe color correction, as well as color matching and color balance effects using the `filter-video` element. The `filter-video` element references an associated `effect` element in the resource section that designates the particular effect. In addition to the Color Board effect, Final Cut Pro 10.4 adds Color Curves, Color Wheel, and Hue/Saturation Curves as color-correction effects.

> **Note**:  In Final Cut Pro 10.2, color correction behaves similarly to other video filters and you can insert it anywhere in a series of video filters.

You can apply color correction with a collection of video-filter masks. The `filter-video-mask` element describes both the filter and the masks and can have up to two `filter-video` child elements. You can apply different color-correction parameters to the inside, the first `filter-video` element, and the outside, the second `filter-video` element, of the mask.

> **Note**:  FCPXML 1.3 and later supports color filtering. Starting in FCPXML 1.5, you can describe color correction, color matching, and color balance effects using the `filter-video` element instead of the `adjust-color` and `color-filter` elements.

### Primary Color Grading

Final Cut Pro supports the American Society of Cinematographers Color Decision List (ASC CDL) format for the exchange of basic primary color grading information between equipment and software from different manufacturers.

FCPXML 1.1 added support for exporting the first primary color correction definition in ASC CDL format. Final Cut Pro v10.2 and later versions export ASC CDL information as an XML comment, as a child of the associated `filter-video` element, if a color correction is applied to a clip in your project. Prior versions of Final Cut Pro exported ASC CDL information with the `info-asc-cdl` element as a child of the associated `clip` element.

The ASC CDL information describes the primary color correction in ASC CDL format as three components: slope, offset, and power. The ASC CDL format represents each component as a vector of red, green, and blue adjustment values, for example, “`1.0 1.0 1.0`”.

The following is an example export of ASC CDL information:

```swift
<filter-video ref="r1" name="Color Correction">    
    <!-- info-asc-cdl:  slope="1.05 1.05 1.05" offset="0.0275 0.0275 0.0275" power="1.25 1.2 1"  -->
</filter-video>
```

## See Also

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
- [Masked Filters](./masked-filters.md)
  Designate a region to which you apply video filter by using a collection of masks.
- [Adjustment Attributes and Effect Parameters](./adjustment-attributes-and-effect-parameters.md)
  Specify values to change adjustment attributes and effects parameters.
- [Animation](./animation.md)
  Create animations by changing specific adjustment attributes and effect parameters over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/filter-video)*