# mapTemplate(_:pitchEndedWithCenter:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that a person stopped pitching the map.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
optional func mapTemplate(_ mapTemplate: CPMapTemplate, pitchEndedWithCenter center: CGPoint)
```

## Parameters

- `mapTemplate`: The   the gesture applies to.
- `center`: A   that indicates the center between two fingers performing the pitch gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:pitchendedwithcenter:))*