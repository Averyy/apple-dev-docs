# Adjustment Attributes and Effect Parameters

**Framework**: Professional-Video-Applications  
**Role**: Article

Specify values to change adjustment attributes and effects parameters.

## Overview

Each adjustment element has attributes that affect the adjustment you make. You specify the values of certain adjustment attributes and effect parameters and change them for the entire duration of the parent element. You can also create animated adjustments by varying attribute values over time.

### Parameter Element

Add a parameter (`param`) element for each adjustment attribute or effect parameter you want to change. You can also use the `param` element to create keyframe animations by changing adjustment attributes and effect parameters over time. For more information on how to create keyframe animations, see [Animation](./animation.md).

The following elements may contain `param` child elements:

- Adjustment elements — `adjust-blend`, `adjust-corners`, `adjust-EQ`, `adjust-panner`, `adjust-stabilization`, `adjust-transform`, `adjust-volume`, `crop-rect`, and `trim-rect`
- Effect elements — `filter-audio` and `filter-video`
- Story elements — `title` and `video`

The `param` element has the following attributes:

| Attribute | Description |
| --- | --- |
| `name` | For adjustments, this case-sensitive string identifies the parent attribute to override. For an effect parameter, this is for informational purposes only. |
| `key` | A string that identifies a parameter in the effect implementation. Final Cut Pro ignores this attribute when you specify the `param` element for an adjustment. |
| `value` | The new value to apply to the adjustment attribute (optional) or the effect parameter. This value overrides the value specified by the parent adjustment attribute. |

For example, the following XML adjusts the audio volume of a clip by –3dB:

```swift
<audio>
   <adjust-volume>
      <param name="amount" value="-3dB" />
   </adjust-volume>
</audio>
```

Some effect parameters allow structured data. Represent the structured data with a series of nested `param` elements as children of the effect parameter you want to override. See the `Lighting` parameter of the 3D text XML snippet in the [text-style](./text-style.md) element for an example.

> **Note**:  Starting in FCPXML 1.5, use structured parameter data to describe the three-dimensional text and other effects.

### data Element

Some adjustments and effects, such as `filter-audio`, `filter-video`, and `mask-isolation`, allow preserving parameter information in an internal binary format. Final Cut Pro uses the `data` element to preserve parameter information of these adjustment and effects elements.

| Data Element | Description |
| --- | --- |
| `data` | Preserves parameter data in binary format. |

| Data Element Attributes | Description |
| --- | --- |
| Key | Indicates whether the data element describes the parameters or the configuration.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) The value can be: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `effectData` — Specifies that the data element is describing parameters.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `effectConfig` — Specifies that the data element is describing configuration.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `effectState` — Specifies that the data element is describing an Audio Units (AU) effect. |

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
- [filter-video](./filter-video.md)
  A filter element that references a video effect.
- [Masked Filters](./masked-filters.md)
  Designate a region to which you apply video filter by using a collection of masks.
- [Animation](./animation.md)
  Create animations by changing specific adjustment attributes and effect parameters over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/adjustment-attributes-and-effect-parameters)*