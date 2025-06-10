# mapTemplate(_:pitchWithCenter:)

**Framework**: CarPlay  
**Kind**: method

Called when a pitch gesture changes. May not be called when connected to some CarPlay systems

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
optional func mapTemplate(_ mapTemplate: CPMapTemplate, pitchWithCenter center: CGPoint)
```

#### Discussion

Tells the delegate that a person is pitching the map.

## Parameters

- `mapTemplate`: The   the gesture applies to.
- `center`: A   that indicates the center between two fingers performing the pitch gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:pitchwithcenter:))*