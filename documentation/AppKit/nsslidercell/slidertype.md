# sliderType

**Framework**: AppKit  
**Kind**: property

The slider type, either linear or circular.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var sliderType: NSSlider.SliderType { get set }
```

#### Discussion

The value of this property is a constant indicating the type of the slider. Possible values are described in [`NSSlider.SliderType`](nsslider/slidertype-swift.enum.md).

When the value of this property is `NSCircularSlider`, then you get a fixed-size circular slider. The minimum value ([`minValue`](nsslidercell/minvalue.md)) is at the top, and the value increases clockwise around the dial. The maximum selectable value is just below [`maxValue`](nsslidercell/maxvalue.md); for example, if [`maxValue`](nsslidercell/maxvalue.md) is 360, you can set the dial up to 359.999.

You can use the [`numberOfTickMarks`](nsslidercell/numberoftickmarks.md) property to display tick marks, and you can use the [`allowsTickMarkValuesOnly`](nsslidercell/allowstickmarkvaluesonly.md) property to specify that values are limited to those values represented by tick marks. You can set this control to regular or small sizes; the mini size is not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/slidertype)*