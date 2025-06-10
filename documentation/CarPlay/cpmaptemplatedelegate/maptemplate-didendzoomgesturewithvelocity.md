# mapTemplate(_:didEndZoomGestureWithVelocity:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that a person stopped zooming the map.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didEndZoomGestureWithVelocity velocity: CGFloat)
```

## Parameters

- `mapTemplate`: The   the gesture applies to.
- `velocity`: The velocity of the zoom gesture in scale factor per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didendzoomgesturewithvelocity:))*