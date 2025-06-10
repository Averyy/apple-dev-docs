# AVRoutePickerView.ButtonState

**Framework**: AVKit  
**Kind**: enum

Constants that describe the available button states.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum ButtonState
```

## Topics

### Button States
- [AVRoutePickerView.ButtonState.normal](avroutepickerview/buttonstate/normal.md)
  The normal, or default, button state.
- [AVRoutePickerView.ButtonState.normalHighlighted](avroutepickerview/buttonstate/normalhighlighted.md)
  The highlighted button state when a mouse-down event occurs inside the button.
- [AVRoutePickerView.ButtonState.active](avroutepickerview/buttonstate/active.md)
  The button state when AirPlay is active.
- [AVRoutePickerView.ButtonState.activeHighlighted](avroutepickerview/buttonstate/activehighlighted.md)
  The highlighted button state when AirPlay is active.
### Initializers
- [init?(rawValue: Int)](avroutepickerview/buttonstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [func setRoutePickerButtonColor(NSColor?, for: AVRoutePickerView.ButtonState)](avroutepickerview/setroutepickerbuttoncolor(_:for:).md)
  Sets the route picker button color for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerview/buttonstate)*