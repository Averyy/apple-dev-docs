# routePickerButtonColor(for:)

**Framework**: AVKit  
**Kind**: method

Returns the color of the picker button for the specified state.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
func routePickerButtonColor(for state: AVRoutePickerView.ButtonState) -> NSColor
```

#### Return Value

A color value for the specified state.

## Parameters

- `state`: The button state.

## See Also

- [var activeTintColor: UIColor!](avroutepickerview/activetintcolor.md)
  The view’s tint color when AirPlay is active.
- [var isRoutePickerButtonBordered: Bool](avroutepickerview/isroutepickerbuttonbordered.md)
  A Boolean value that indicates whether the route picker button has a border.
- [var prioritizesVideoDevices: Bool](avroutepickerview/prioritizesvideodevices.md)
  A Boolean value that indicates whether the route picker sorts video output devices to the top of the list.
- [var routePickerButtonStyle: AVRoutePickerViewButtonStyle](avroutepickerview/routepickerbuttonstyle.md)
  The button style for the route picker.
- [enum AVRoutePickerViewButtonStyle](avroutepickerviewbuttonstyle.md)
  Constants that define the button styles a route picker view supports.
- [func setRoutePickerButtonColor(NSColor?, for: AVRoutePickerView.ButtonState)](avroutepickerview/setroutepickerbuttoncolor(_:for:).md)
  Sets the route picker button color for the specified state.
- [AVRoutePickerView.ButtonState](avroutepickerview/buttonstate.md)
  Constants that describe the available button states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerview/routepickerbuttoncolor(for:))*