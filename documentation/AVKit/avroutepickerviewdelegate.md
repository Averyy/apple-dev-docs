# AVRoutePickerViewDelegate

**Framework**: AVKit  
**Kind**: protocol

A protocol that defines the methods to adopt to respond to route picker view presentation events.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 11.0+

## Declaration

```swift
protocol AVRoutePickerViewDelegate : NSObjectProtocol
```

## Topics

### Presenting Routes
- [func routePickerViewWillBeginPresentingRoutes(AVRoutePickerView)](avroutepickerviewdelegate/routepickerviewwillbeginpresentingroutes(_:).md)
  Tells the delegate that the route picker view is about to begin presenting routes to the user.
- [func routePickerViewDidEndPresentingRoutes(AVRoutePickerView)](avroutepickerviewdelegate/routepickerviewdidendpresentingroutes(_:).md)
  Tells the delegate when the route picker view finishes presenting routes to the user.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any AVRoutePickerViewDelegate)?](avroutepickerview/delegate.md)
  The delegate object for the route picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerviewdelegate)*