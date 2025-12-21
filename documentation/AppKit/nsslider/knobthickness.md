# knobThickness

**Framework**: AppKit  
**Kind**: property

The knob’s thickness, in pixels.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var knobThickness: CGFloat { get }
```

#### Discussion

The thickness is defined to be the extent of the knob along the long dimension of the bar. In a vertical slider, a knob’s thickness is its height; in a horizontal slider, a knob’s thickness is its width.

## See Also

- [var sliderType: NSSlider.SliderType](nsslider/slidertype-swift.property.md)
  The type of the slider, such as vertical or circular.
- [NSSlider.SliderType](nsslider/slidertype-swift.enum.md)
  The types of sliders, used by [`sliderType`](nsslidercell/slidertype.md).
- [var altIncrementValue: Double](nsslider/altincrementvalue.md)
  The amount by which the slider changes its value when the user Option-drags the slider knob.
- [var isVertical: Bool](nsslider/isvertical.md)
  An integer indicating the orientation (horizontal or vertical) of the slider.
- [var trackFillColor: NSColor?](nsslider/trackfillcolor.md)
  The color of the filled portion of the slider track, in appearances that support it.
- [var tintProminence: NSTintProminence](nsslider/tintprominence.md)
  The tint prominence of the slider. The automatic behavior for a regular slider tints its track fill, while a slider with tick marks is untinted. Setting the tint prominence will override this default behavior and choose an explicit track fill tint behavior. See [`NSTintProminence`](nstintprominence.md) for a list of possible values.
- [enum NSTintProminence](nstintprominence.md)
  Controls how strongly the tint color applies in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/knobthickness)*