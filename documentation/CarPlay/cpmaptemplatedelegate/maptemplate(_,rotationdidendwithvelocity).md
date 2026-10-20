# mapTemplate(_:rotationDidEndWithVelocity:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a person stopped rotating the map.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, rotationDidEndWithVelocity velocity: CGFloat)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate rotationDidEndWithVelocity:(CGFloat) velocity;
```

## Parameters

- `mapTemplate`: The [`CPMapTemplate`](../cpmaptemplate.md) the gesture applies to.
- `velocity`: The velocity of the rotation gesture in radians per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:rotationdidendwithvelocity:))*