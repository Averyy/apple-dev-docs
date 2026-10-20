# routePickerViewDidEndPresentingRoutes(_:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the route picker view finishes presenting routes to the user.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 11.0+

## Declaration

```swift
optional func routePickerViewDidEndPresentingRoutes(_ routePickerView: AVRoutePickerView)
```

```objc
- (void) routePickerViewDidEndPresentingRoutes:(AVRoutePickerView *) routePickerView;
```

## Parameters

- `routePickerView`: The route picker view.

## See Also

### Presenting routes
- [func routePickerViewWillBeginPresentingRoutes(AVRoutePickerView)](./routepickerviewwillbeginpresentingroutes%28_%29.md)
  Tells the delegate that the route picker view is about to begin presenting routes to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerviewdelegate/routepickerviewdidendpresentingroutes(_:))*