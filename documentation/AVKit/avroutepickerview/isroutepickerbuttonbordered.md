# isRoutePickerButtonBordered

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the route picker button has a border.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var isRoutePickerButtonBordered: Bool { get set }
```

```objc
@property (nonatomic, getter=isRoutePickerButtonBordered) BOOL routePickerButtonBordered;
```

## Discussion

The default value is `true`.

## See Also

### Configuring the route picker view
- [var activeTintColor: UIColor!](./activetintcolor.md)
  The view’s tint color when AirPlay is active.
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
- [AVRoutePickerView.ButtonState](./buttonstate.md)
  Constants that describe the available button states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerview/isroutepickerbuttonbordered)*