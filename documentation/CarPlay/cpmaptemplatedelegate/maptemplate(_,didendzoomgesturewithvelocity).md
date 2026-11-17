# mapTemplate(_:didEndZoomGestureWithVelocity:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a person stopped zooming the map.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didEndZoomGestureWithVelocity velocity: CGFloat)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate didEndZoomGestureWithVelocity:(CGFloat) velocity;
```

## Parameters

- `mapTemplate`: The [`CPMapTemplate`](../cpmaptemplate.md) the gesture applies to.
- `velocity`: The velocity of the zoom gesture in scale factor per second.

## See Also

### Changing the zoom level
- [func mapTemplateDidBeginZoomGesture(CPMapTemplate)](./maptemplatedidbeginzoomgesture%28_%29.md)
  Tells the delegate that the zoom gesture started.
- [func mapTemplate(CPMapTemplate, didUpdateZoomGestureWithCenter: CGPoint, scale: CGFloat, velocity: CGFloat)](./maptemplate%28_,didupdatezoomgesturewithcenter,scale,velocity%29.md)
  Tells the delegate that a person is zooming on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didendzoomgesturewithvelocity:))*