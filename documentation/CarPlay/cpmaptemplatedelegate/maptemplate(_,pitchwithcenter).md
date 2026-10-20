# mapTemplate(_:pitchWithCenter:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Called when a pitch gesture changes. May not be called when connected to some CarPlay systems

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, pitchWithCenter center: CGPoint)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate pitchWithCenter:(CGPoint) center;
```

#### Discussion

Tells the delegate that a person is pitching the map.

## Parameters

- `mapTemplate`: The [`CPMapTemplate`](../cpmaptemplate.md) the gesture applies to.
- `center`: A `CGPoint` that indicates the center between two fingers performing the pitch gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:pitchwithcenter:))*