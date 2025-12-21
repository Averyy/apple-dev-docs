# sliderType

**Framework**: AppKit  
**Kind**: property

The type of the slider, such as vertical or circular.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var sliderType: NSSlider.SliderType { get set }
```

#### Discussion

See [`NSSlider.SliderType`](nsslider/slidertype-swift.enum.md) for possible values.

## See Also

- [NSSlider.SliderType](nsslider/slidertype-swift.enum.md)
  The types of sliders, used by [`sliderType`](nsslidercell/slidertype.md).
- [var altIncrementValue: Double](nsslider/altincrementvalue.md)
  The amount by which the slider changes its value when the user Option-drags the slider knob.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/slidertype-swift.property)*