# mapTemplateDidBeginZoomGesture(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the zoom gesture started.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
optional func mapTemplateDidBeginZoomGesture(_ mapTemplate: CPMapTemplate)
```

```objc
- (void) mapTemplateDidBeginZoomGesture:(CPMapTemplate *) mapTemplate;
```

## Parameters

- `mapTemplate`: The [`CPMapTemplate`](../cpmaptemplate.md) the gesture applies to.

## See Also

### Changing the zoom level
- [func mapTemplate(CPMapTemplate, didUpdateZoomGestureWithCenter: CGPoint, scale: CGFloat, velocity: CGFloat)](./maptemplate%28_,didupdatezoomgesturewithcenter,scale,velocity%29.md)
  Tells the delegate that a person is zooming on the map.
- [func mapTemplate(CPMapTemplate, didEndZoomGestureWithVelocity: CGFloat)](./maptemplate%28_,didendzoomgesturewithvelocity%29.md)
  Tells the delegate that a person stopped zooming the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplatedidbeginzoomgesture(_:))*