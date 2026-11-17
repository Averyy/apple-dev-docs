# mapTemplateDidBeginRotationGesture(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the rotation gesture started.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
optional func mapTemplateDidBeginRotationGesture(_ mapTemplate: CPMapTemplate)
```

```objc
- (void) mapTemplateDidBeginRotationGesture:(CPMapTemplate *) mapTemplate;
```

## Parameters

- `mapTemplate`: The [`CPMapTemplate`](../cpmaptemplate.md) the gesture applies to.

## See Also

### Rotating the map
- [func mapTemplate(CPMapTemplate, didRotateWithCenter: CGPoint, rotation: CGFloat, velocity: CGFloat)](./maptemplate%28_,didrotatewithcenter,rotation,velocity%29.md)
  Tells the delegate that a person is rotating the map.
- [func mapTemplate(CPMapTemplate, rotationDidEndWithVelocity: CGFloat)](./maptemplate%28_,rotationdidendwithvelocity%29.md)
  Tells the delegate that a person stopped rotating the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplatedidbeginrotationgesture(_:))*