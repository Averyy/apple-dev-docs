# isRoutePickerButtonBordered

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the route picker button has a border.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
var isRoutePickerButtonBordered: Bool { get set }
```

#### Discussion

The default value is `true`.

## See Also

- [var activeTintColor: UIColor!](avroutepickerview/activetintcolor.md)
  The view’s tint color when AirPlay is active.
- [var prioritizesVideoDevices: Bool](avroutepickerview/prioritizesvideodevices.md)
  A Boolean value that indicates whether the route picker sorts video output devices to the top of the list.
- [var routePickerButtonStyle: AVRoutePickerViewButtonStyle](avroutepickerview/routepickerbuttonstyle.md)
  The button style for the route picker.
- [enum AVRoutePickerViewButtonStyle](avroutepickerviewbuttonstyle.md)
  Constants that define the button styles a route picker view supports.
- [func routePickerButtonColor(for: AVRoutePickerView.ButtonState) -> NSColor](avroutepickerview/routepickerbuttoncolor(for:).md)
  Returns the color of the picker button for the specified state.
- [func setRoutePickerButtonColor(NSColor?, for: AVRoutePickerView.ButtonState)](avroutepickerview/setroutepickerbuttoncolor(_:for:).md)
  Sets the route picker button color for the specified state.
- [AVRoutePickerView.ButtonState](avroutepickerview/buttonstate.md)
  Constants that describe the available button states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerview/isroutepickerbuttonbordered)*