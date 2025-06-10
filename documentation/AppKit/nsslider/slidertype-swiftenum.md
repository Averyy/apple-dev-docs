# NSSlider.SliderType

**Framework**: AppKit  
**Kind**: enum

The types of sliders, used by [`sliderType`](nsslidercell/slidertype.md).

**Availability**:
- macOS ?+

## Declaration

```swift
enum SliderType
```

## Topics

### Enumeration Cases
- [NSSlider.SliderType.circular](nsslider/slidertype-swift.enum/circular.md)
  A dial representing an angular range.
- [NSSlider.SliderType.linear](nsslider/slidertype-swift.enum/linear.md)
  A bar representing a range, and a knob indicating the currently selected value.
### Initializers
- [init?(rawValue: UInt)](nsslider/slidertype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var sliderType: NSSlider.SliderType](nsslider/slidertype-swift.property.md)
  The type of the slider, such as vertical or circular.
- [var altIncrementValue: Double](nsslider/altincrementvalue.md)
  The amount by which the slider changes its value when the user Option-drags the slider knob.
- [var knobThickness: CGFloat](nsslider/knobthickness.md)
  The knob’s thickness, in pixels.
- [var isVertical: Bool](nsslider/isvertical.md)
  An integer indicating the orientation (horizontal or vertical) of the slider.
- [var trackFillColor: NSColor?](nsslider/trackfillcolor.md)
  The color of the filled portion of the slider track, in appearances that support it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/slidertype-swift.enum)*