# AVRoutePickerView.ButtonState

**Framework**: AVKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the available button states.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum ButtonState
```

```c
enum AVRoutePickerViewButtonState : NSInteger;
```

## Topics

### Creating a button state
- [init?(rawValue: Int)](./buttonstate/init%28rawvalue%29.md)
### Button states
- [AVRoutePickerView.ButtonState.normal](./buttonstate/normal.md)
  The normal, or default, button state.
- [AVRoutePickerView.ButtonState.normalHighlighted](./buttonstate/normalhighlighted.md)
  The highlighted button state when a mouse-down event occurs inside the button.
- [AVRoutePickerView.ButtonState.active](./buttonstate/active.md)
  The button state when AirPlay is active.
- [AVRoutePickerView.ButtonState.activeHighlighted](./buttonstate/activehighlighted.md)
  The highlighted button state when AirPlay is active.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the route picker view
- [var activeTintColor: UIColor!](./activetintcolor.md)
  The view’s tint color when AirPlay is active.
- [var isRoutePickerButtonBordered: Bool](./isroutepickerbuttonbordered.md)
  A Boolean value that indicates whether the route picker button has a border.
- [var prioritizesVideoDevices: Bool](./prioritizesvideodevices.md)
  A Boolean value that indicates whether the route picker sorts video output devices to the top of the list.
- [var routePickerButtonStyle: AVRoutePickerViewButtonStyle](./routepickerbuttonstyle.md)
  The button style for the route picker.
- [enum AVRoutePickerViewButtonStyle](../avroutepickerviewbuttonstyle.md)
  Constants that define the button styles a route picker view supports.
- [func routePickerButtonColor(for: AVRoutePickerView.ButtonState) -> NSColor](./routepickerbuttoncolor%28for%29.md)
  Returns the color of the picker button for the specified state.
- [func setRoutePickerButtonColor(NSColor?, for: AVRoutePickerView.ButtonState)](./setroutepickerbuttoncolor%28_,for%29.md)
  Sets the route picker button color for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerview/buttonstate)*