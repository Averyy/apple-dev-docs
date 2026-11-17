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

## See Also

### Changing the camera pitch
- [func mapTemplateDidBeginPitchGesture(CPMapTemplate)](./maptemplatedidbeginpitchgesture%28_%29.md)
  Tells the delegate that the pitch gesture started.
- [func mapTemplate(CPMapTemplate, pitchWithCenter: CGPoint)](./maptemplate%28_,pitchwithcenter%29.md)
  Called when a pitch gesture changes. May not be called when connected to some CarPlay systems


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:pitchendedwithcenter:))*