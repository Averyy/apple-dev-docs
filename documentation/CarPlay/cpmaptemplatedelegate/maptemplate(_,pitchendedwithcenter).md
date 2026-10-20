# mapTemplate(_:pitchEndedWithCenter:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a person stopped pitching the map.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, pitchEndedWithCenter center: CGPoint)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate pitchEndedWithCenter:(CGPoint) center;
```

## Parameters

- `mapTemplate`: The [`CPMapTemplate`](../cpmaptemplate.md) the gesture applies to.
- `center`: A `CGPoint` that indicates the center between two fingers performing the pitch gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:pitchendedwithcenter:))*