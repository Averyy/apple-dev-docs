# mapTemplate(_:didUpdateZoomGestureWithCenter:scale:velocity:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that a person is zooming on the map.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didUpdateZoomGestureWithCenter center: CGPoint, scale: CGFloat, velocity: CGFloat)
```

## Parameters

- `mapTemplate`: The [`CPMapTemplate`](cpmaptemplate.md) the gesture applies to.
- `center`: A `CGPoint` that indicates the center point of the zoom.
- `scale`: A `CGFloat` that indicates the scale factor relative to the zoom gesture in screen coordinates.
- `velocity`: The velocity of the zoom gesture in scale factor per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didupdatezoomgesturewithcenter:scale:velocity:))*