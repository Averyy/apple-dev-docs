# mapTemplate(_:rotationDidEndWithVelocity:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that a person stopped rotating the map.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
optional func mapTemplate(_ mapTemplate: CPMapTemplate, rotationDidEndWithVelocity velocity: CGFloat)
```

## Parameters

- `mapTemplate`: The   the gesture applies to.
- `velocity`: The velocity of the rotation gesture in radians per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:rotationdidendwithvelocity:))*