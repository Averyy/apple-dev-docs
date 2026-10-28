# Adjustment Elements

**Framework**: Professional-Video-Applications

Alter the audio and video output of story elements by using adjustment elements.

## Overview

You can apply adjustment to change specific aspects of audio and video, in particular:

- Audio adjustments, such as audio volume and panning, loudness control, and EQ.
- Video adjustments, including geometrical video transformations, such as position, scale, rotation, crop, pan and zoom, blend mode, and size conforming.
- 360 adjustments, such as where to place a non-360 clip in a 360 project, the viewable portion of a 360 clip in a non-360 project, and the default orientation of a 360 clip in a 360 project using the 360 adjustment elements.

> **Note**:  Starting in FCPXML 1.3, there is support for color adjustments, audio adjustment, and video adjustments.

Each adjustment element has attributes that affect the audio or video adjustments you want to make. Specify the values to override; all other values remain at their default settings. Create animated adjustments by varying attribute values over time. For information on how to adjust attribute values over time, see [Animation](./animation.md).

Some adjustment attributes expect a multidimensional (or compound) value, such as an (x,y) point. Specify these attributes with a space separating each value. For example, specify the two-dimensional values (0,0) or (10,-25) as “0 0” or “10 -25”.

> **Note**:  Final Cut Pro applies audio adjustments to the entire multicam clip (specified by the `mc-clip` element), whereas Final Cut Pro applies visual adjustments to each angle (specified by the `mc-source` element). In FCPXML 1.3 and earlier, Final Cut Pro applies both visual adjustments and audio adjustments to the entire multicam clip (on to the `mc-clip` element).

## Topics

### Audio Adjustment Elements
- [adjust-EQ](./adjust-eq.md)
  Specifies the equalization to apply to a clip.
- [adjust-humReduction](./adjust-humreduction.md)
  Applies hum reduction at the frequency, either 50 or 60 Hz, that the frequency attribute specifies.
- [adjust-loudness](./adjust-loudness.md)
  Modifies the loudness. 
- [adjust-matchEQ](./adjust-matcheq.md)
  Specifies the equalization to apply, in an internal format, to match another clip’s frequency characteristics.
- [adjust-noiseReduction](./adjust-noisereduction.md)
  Applies noise reduction with a value between 0 and 100 that the amount attribute specifies.
- [adjust-panner](./adjust-panner.md)
  Modifies the audio-panning levels.
- [adjust-volume](./adjust-volume.md)
  Modifies the volume of a clip in dB.
### Video Adjustment Elements
- [adjust-blend](./adjust-blend.md)
  Modifies the compositing blend mode and opacity percentage.
- [adjust-cinematic](./adjust-cinematic.md)
  Describes the focus of Cinematic Video clips.
- [adjust-conform](./adjust-conform.md)
  Modifies the image size of a clip.
- [adjust-corners](./adjust-corners.md)
  Modifies the corners of a visible image.
- [adjust-crop](./adjust-crop.md)
  Modifies the visible image width and height.
- [adjust-rollingShutter](./adjust-rollingshutter.md)
  Specifies the rolling shutter reduction to apply to a clip.
- [adjust-stabilization](./adjust-stabilization.md)
  Specifies the stabilization to aplly to a clip.
- [adjust-transform](./adjust-transform.md)
  Modifies the visible image through resizing, moving, or rotating.
### 360 Adjustment Elements
- [adjust-360-transform](./adjust-360-transform.md)
  Specifies where to position a non-360 clip in a 360 project’s sphere.
- [adjust-orientation](./adjust-orientation.md)
  Specifies what part of a spherical clip to use in a non-360 project.
- [adjust-reorient](./adjust-reorient.md)
  Reorients a spherical clip within a 360 project. 

## See Also

### Adjustment and Effects Elements
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/adjustment-elements)*