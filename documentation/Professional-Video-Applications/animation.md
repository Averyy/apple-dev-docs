# Animation

**Framework**: Professional-Video-Applications

Create animations by changing specific adjustment attributes and effect parameters over time.

## Overview

You can create animations with a [Parameter Element](./adjustment-attributes-and-effect-parameters.md#Parameter-Element) for the attribute or parameter to animate, along with a [keyframeAnimation](./keyframeanimation.md) element that has a series of `keyframe` elements, each of which defines a value at a point in time.

To produce a keyframe animation, specify the time points and values for each keyframe using the time and value attributes of the `keyframe` element. The Final Cut Pro application interpolates the values between them.

The following example performs a position and scale transform adjustment animation using keyframes:

```swift
<adjust-transform position="-10 10">
   <param name="position">
      <keyframeAnimation>
         <keyframe time="0s" value="-5 10" />
         <keyframe time="10s" value="10 20" />
      </keyframeAnimation>
   </param>
   <param name="scale">
      <keyframeAnimation>
         <keyframe time="0s" value="1 1" />
         <keyframe time="10s" value="0.75 0.75" />
      </keyframeAnimation>
   </param>
</adjust-transform>
```

Initially, when time is equal to  0 seconds (time=0s), the frame is moved left 5 percent and up 10 percent `(“-5 10”)` of the project’s height from the original location, with no change in size `(“1 1”)`. When time is equal to 10 seconds (time=10s), the frame has moved 10 percent right and 20 percent up `(“10 20”)` of the project’s height from the original location, with a 25 percent `(“0.75 0.75”)` reduction in size from the original `(“1 1”)`. For more information on the `adjust-transform` element, see [Video Adjustment Elements](./adjustment-elements.md#Video-Adjustment-Elements).

Final Cut Pro determines the parameter value based on the following priority (with 1 being the highest priority):

- The `value` and `time` attributes of the `keyframe` element, for a particular time
- The `value` attribute of the `param` element
- The respective attribute of the adjustment, if applicable

In the previous example, it doesn’t matter that the `position` attribute of the `adjust-transform` element has a value of “`-10 10`”,  because the keyframe defined at when time is equal to 0s (`time=0s)` (in the `keyframe` element) takes priority and overrides the value to “`-5 10`”.

## Topics

### Keyframe Animation Elements
- [keyframeAnimation](./keyframeanimation.md)
  Specifies an animation path for each keyframe.

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
- [Adjustment Attributes and Effect Parameters](./adjustment-attributes-and-effect-parameters.md)
  Specify values to change adjustment attributes and effects parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/animation)*