# altIncrementValue

**Framework**: AppKit  
**Kind**: property

The amount by which the slider changes its value when the user Option-drags the slider knob.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var altIncrementValue: Double { get set }
```

#### Discussion

By default, the value of this property is `-1.0`, and the slider behaves no differently with the Option key down than with it up. The value of this property must fit the range of values the slider can represent—for example, if the slider has a minimum value of `5` and a maximum value of `10`, the value should be between `0` and `5`.

## See Also

- [var sliderType: NSSlider.SliderType](nsslider/slidertype-swift.property.md)
  The type of the slider, such as vertical or circular.
- [NSSlider.SliderType](nsslider/slidertype-swift.enum.md)
  The types of sliders, used by [`sliderType`](nsslidercell/slidertype.md).
- [var knobThickness: CGFloat](nsslider/knobthickness.md)
  The knob’s thickness, in pixels.
- [var isVertical: Bool](nsslider/isvertical.md)
  An integer indicating the orientation (horizontal or vertical) of the slider.
- [var trackFillColor: NSColor?](nsslider/trackfillcolor.md)
  The color of the filled portion of the slider track, in appearances that support it.
- [var tintProminence: NSTintProminence](nsslider/tintprominence.md)
  The tint prominence of the slider. The automatic behavior for a regular slider tints its track fill, while a slider with tick marks is untinted. Setting the tint prominence will override this default behavior and choose an explicit track fill tint behavior. See [`NSTintProminence`](nstintprominence.md) for a list of possible values.
- [enum NSTintProminence](nstintprominence.md)
  Controls how strongly the tint color applies in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/altincrementvalue)*