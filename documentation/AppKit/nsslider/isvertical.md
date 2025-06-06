# isVertical

**Framework**: AppKit  
**Kind**: property

An integer indicating the orientation (horizontal or vertical) of the slider.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var vertical: Bool { get set }
```

#### Discussion

The value of this property is `1` if the slider is vertical, `0` if it’s horizontal, and `-1` if the orientation is unknown (for example, if the slider hasn’t been displayed yet). A slider is defined as vertical if its height is greater than its width.

## See Also

- [var sliderType: NSSlider.SliderType](nsslider/slidertype-swift.property.md)
  The type of the slider, such as vertical or circular.
- [NSSlider.SliderType](nsslider/slidertype-swift.enum.md)
  The types of sliders, used by [`sliderType`](nsslidercell/slidertype.md).
- [var altIncrementValue: Double](nsslider/altincrementvalue.md)
  The amount by which the slider changes its value when the user Option-drags the slider knob.
- [var knobThickness: CGFloat](nsslider/knobthickness.md)
  The knob’s thickness, in pixels.
- [var trackFillColor: NSColor?](nsslider/trackfillcolor.md)
  The color of the filled portion of the slider track, in appearances that support it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/isvertical)*