# setRoutePickerButtonColor(_:for:)

**Framework**: AVKit  
**Kind**: method

Sets the route picker button color for the specified state.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
func setRoutePickerButtonColor(_ color: NSColor?, for state: AVRoutePickerView.ButtonState)
```

## Parameters

- `color`: The route picker button color to set.
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
- [func routePickerButtonColor(for: AVRoutePickerView.ButtonState) -> NSColor](avroutepickerview/routepickerbuttoncolor(for:).md)
  Returns the color of the picker button for the specified state.
- [AVRoutePickerView.ButtonState](avroutepickerview/buttonstate.md)
  Constants that describe the available button states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerview/setroutepickerbuttoncolor(_:for:))*