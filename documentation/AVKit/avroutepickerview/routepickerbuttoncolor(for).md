# routePickerButtonColor(for:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Returns the color of the picker button for the specified state.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func routePickerButtonColor(for state: AVRoutePickerView.ButtonState) -> NSColor
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (UIColor *) routePickerButtonColorForState:(AVRoutePickerViewButtonState) state;
```

*macOS*

```objc
- (NSColor *) routePickerButtonColorForState:(AVRoutePickerViewButtonState) state;
```

#### Return Value

A color value for the specified state.

## Parameters

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
- [func setRoutePickerButtonColor(NSColor?, for: AVRoutePickerView.ButtonState)](./setroutepickerbuttoncolor%28_,for%29.md)
  Sets the route picker button color for the specified state.
- [AVRoutePickerView.ButtonState](./buttonstate.md)
  Constants that describe the available button states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerview/routepickerbuttoncolor(for:))*