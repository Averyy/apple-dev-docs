# mapTemplateDidBeginPitchGesture(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the pitch gesture started.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
optional func mapTemplateDidBeginPitchGesture(_ mapTemplate: CPMapTemplate)
```

```objc
- (void) mapTemplateDidBeginPitchGesture:(CPMapTemplate *) mapTemplate;
```

## Parameters

- `mapTemplate`: The [`CPMapTemplate`](../cpmaptemplate.md) the gesture applies to.

## See Also

### Changing the camera pitch
- [func mapTemplate(CPMapTemplate, pitchWithCenter: CGPoint)](./maptemplate%28_,pitchwithcenter%29.md)
  Called when a pitch gesture changes. May not be called when connected to some CarPlay systems
- [func mapTemplate(CPMapTemplate, pitchEndedWithCenter: CGPoint)](./maptemplate%28_,pitchendedwithcenter%29.md)
  Tells the delegate that a person stopped pitching the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplatedidbeginpitchgesture(_:))*