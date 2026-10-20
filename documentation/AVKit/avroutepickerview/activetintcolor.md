# activeTintColor

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The view’s tint color when AirPlay is active.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+

## Declaration

```swift
var activeTintColor: UIColor! { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, strong, null_resettable) UIColor * activeTintColor;
```

*macOS*

```objc
@property (nonatomic, strong, null_resettable) NSColor * activeTintColor;
```

## See Also

### Configuring the route picker view
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
- [AVRoutePickerView.ButtonState](./buttonstate.md)
  Constants that describe the available button states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerview/activetintcolor)*