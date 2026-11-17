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

## Discussion

Tells the delegate that a person is pitching the map.

## Parameters

- `mapTemplate`: The [`CPMapTemplate`](../cpmaptemplate.md) the gesture applies to.
- `center`: A `CGPoint` that indicates the center between two fingers performing the pitch gesture.

## See Also

### Changing the camera pitch
- [func mapTemplateDidBeginPitchGesture(CPMapTemplate)](./maptemplatedidbeginpitchgesture%28_%29.md)
  Tells the delegate that the pitch gesture started.
- [func mapTemplate(CPMapTemplate, pitchEndedWithCenter: CGPoint)](./maptemplate%28_,pitchendedwithcenter%29.md)
  Tells the delegate that a person stopped pitching the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:pitchwithcenter:))*