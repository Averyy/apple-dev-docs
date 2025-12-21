# mapTemplate(_:didRotateWithCenter:rotation:velocity:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that a person is rotating the map.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didRotateWithCenter center: CGPoint, rotation: CGFloat, velocity: CGFloat)
```

## Parameters

- `mapTemplate`: The   the gesture applies to.
- `center`: A   that indicates the center between two fingers performing the rotation gesture.
- `rotation`: A   that indicates the rotation of the gesture in radians.
- `velocity`: The velocity of the rotation gesture in radians per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didrotatewithcenter:rotation:velocity:))*