# NSSlider.SliderType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The types of sliders, used by [`sliderType`](../nsslidercell/slidertype.md).

**Availability**:
- macOS

## Declaration

```swift
enum SliderType
```

```c
enum NSSliderType : NSUInteger;
```

## Topics

### Enumeration Cases
- [NSSlider.SliderType.circular](./slidertype-swift.enum/circular.md)
  A dial representing an angular range.
- [NSSlider.SliderType.linear](./slidertype-swift.enum/linear.md)
  A bar representing a range, and a knob indicating the currently selected value.
- [NSLinearSlider](../nslinearslider.md)
- [NSCircularSlider](../nscircularslider.md)
### Initializers
- [init?(rawValue: UInt)](./slidertype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the slider’s appearance
- [var sliderType: NSSlider.SliderType](./slidertype-swift.property.md)
  The type of the slider, such as vertical or circular.
- [var altIncrementValue: Double](./altincrementvalue.md)
  The amount by which the slider changes its value when the user Option-drags the slider knob.
- [var knobThickness: CGFloat](./knobthickness.md)
  The knob’s thickness, in pixels.
- [var isVertical: Bool](./isvertical.md)
  An integer indicating the orientation (horizontal or vertical) of the slider.
- [var trackFillColor: NSColor?](./trackfillcolor.md)
  The color of the filled portion of the slider track, in appearances that support it.
- [var tintProminence: NSTintProminence](./tintprominence.md)
  The tint prominence of the slider. The automatic behavior for a regular slider tints its track fill, while a slider with tick marks is untinted. Setting the tint prominence will override this default behavior and choose an explicit track fill tint behavior. See [`NSTintProminence`](../nstintprominence.md) for a list of possible values.
- [enum NSTintProminence](../nstintprominence.md)
  Controls how strongly the tint color applies in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/slidertype-swift.enum)*