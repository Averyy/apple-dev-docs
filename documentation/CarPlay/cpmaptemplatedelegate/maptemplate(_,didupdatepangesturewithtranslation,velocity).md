# mapTemplate(_:didUpdatePanGestureWithTranslation:velocity:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the pan gesture changed.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didUpdatePanGestureWithTranslation translation: CGPoint, velocity: CGPoint)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate didUpdatePanGestureWithTranslation:(CGPoint) translation velocity:(CGPoint) velocity;
```

#### Discussion

CarPlay doesn’t call this method when connected to some CarPlay systems.

## Parameters

- `mapTemplate`: The current map template.
- `translation`: The updated translation point.
- `velocity`: The velocity of the pan gesture.

## See Also

### Panning the Map
- [func mapTemplateDidShowPanningInterface(CPMapTemplate)](./maptemplatedidshowpanninginterface%28_%29.md)
  Tells the delegate that the panning interface is visible on the map.
- [func mapTemplateWillDismissPanningInterface(CPMapTemplate)](./maptemplatewilldismisspanninginterface%28_%29.md)
  Tells the delegate that the panning interface will disappear from the map.
- [func mapTemplateDidDismissPanningInterface(CPMapTemplate)](./maptemplatediddismisspanninginterface%28_%29.md)
  Tells the delegate that the panning interface is no longer visible on the map.
- [func mapTemplateDidBeginPanGesture(CPMapTemplate)](./maptemplatedidbeginpangesture%28_%29.md)
  Tells the delegate that the pan gesture has started.
- [func mapTemplate(CPMapTemplate, panBeganWith: CPMapTemplate.PanDirection)](./maptemplate%28_,panbeganwith%29.md)
  Tells the delegate that the user is starting to pan the map.
- [func mapTemplate(CPMapTemplate, panWith: CPMapTemplate.PanDirection)](./maptemplate%28_,panwith%29.md)
  Tells the delegate that the user is panning in a certain direction on the map.
- [func mapTemplate(CPMapTemplate, panEndedWith: CPMapTemplate.PanDirection)](./maptemplate%28_,panendedwith%29.md)
  Tells the delegate that the user stopped panning the map.
- [CPMapTemplate.PanDirection](../cpmaptemplate/pandirection.md)
  The directions a user can pan (or move) a map displayed on the CarPlay screen.
- [func mapTemplate(CPMapTemplate, didEndPanGestureWithVelocity: CGPoint)](./maptemplate%28_,didendpangesturewithvelocity%29.md)
  Tells the delegate that the pan gesture ended with the specified velocity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didupdatepangesturewithtranslation:velocity:))*