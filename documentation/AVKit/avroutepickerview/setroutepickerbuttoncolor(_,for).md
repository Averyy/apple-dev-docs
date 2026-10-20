# setRoutePickerButtonColor(_:for:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Sets the route picker button color for the specified state.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func setRoutePickerButtonColor(_ color: NSColor?, for state: AVRoutePickerView.ButtonState)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (void) setRoutePickerButtonColor:(UIColor *) color forState:(AVRoutePickerViewButtonState) state;
```

*macOS*

```objc
- (void) setRoutePickerButtonColor:(NSColor *) color forState:(AVRoutePickerViewButtonState) state;
```

## Parameters

- `color`: The route picker button color to set.
- `state`: The button state.

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
- [AVRoutePickerView.ButtonState](./buttonstate.md)
  Constants that describe the available button states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerview/setroutepickerbuttoncolor(_:for:))*