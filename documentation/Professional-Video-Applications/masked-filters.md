# Masked Filters

**Framework**: Professional-Video-Applications

Designate a region to which you apply video filter by using a collection of masks.

## Overview

Use a `filter-video-mask` element to apply video filters to a portion of the image described as a mask, or apply two different filters, one inside the mask and one outside. Together, the  Mask Elements define a single region to which the effect applies. The actual video filter is described with a `video-filter` element as a child of the `filter-video-mask` element.

> **Note**:  FCPXML 1.5 added support to apply video filters to a region defined by a collection of masks.

A mask may consist of multiple shapes or color isolations. For a color correction filter, in addition to the correction you apply inside the mask, there may be another set of correction parameters to apply outside the mask. The code below represents a masked video filter with a single shape mask.

```swift
 <filter-video-mask>
    <mask-shape name="Shape Mask" blendMode="add">
       <param name="Radius" key="160" value="750 150"/>
       <param name="Curvature" key="159" value="0.7"/>
       <param name="Feather" key="102" value="170"/>
       <param name="Transforms" key="200">
          <param name="Position" key="201" value="10 110"/>
          <param name="Rotation" key="202" value="14"/>
       </param>
     </mask-shape>
     <filter-video ref="100"/>
</filter-video-mask>
```

The next code example represents a color-correction filter with a single shape mask and different correction parameters that the example applies inside and outside of the mask. The first `filter-video` element represents the inner correction and the second corresponds to the outer correction.

```swift
<filter-video-mask>
     <mask-shape name="Shape Mask" blendMode="add">
        <param name="Curvature" key="159" value="0.7"/>
         <param name="Transforms" key="200">
            <param name="Position" key="201" value="260 -30"/>
          </param>
      </mask-shape>
      <filter-video ref="1000">
           <param name="color_global" value="0.2 0.8"/>
      </filter-video>
      <filter-video ref="1000"/>
           <param name="color_highlight" value="0.3 0.6"/>
       </filter-video>
 </filter-video-mask>
```

## Topics

### Mask Elements
- [mask-isolation](./mask-isolation.md)
  Describes a color isolation mask.
- [mask-shape](./mask-shape.md)
  Describes a shape that serves as a mask.

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
- [Adjustment Attributes and Effect Parameters](./adjustment-attributes-and-effect-parameters.md)
  Specify values to change adjustment attributes and effects parameters.
- [Animation](./animation.md)
  Create animations by changing specific adjustment attributes and effect parameters over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/masked-filters)*