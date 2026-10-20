# mapTemplateDidShowPanningInterface(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the panning interface is visible on the map.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplateDidShowPanningInterface(_ mapTemplate: CPMapTemplate)
```

```objc
- (void) mapTemplateDidShowPanningInterface:(CPMapTemplate *) mapTemplate;
```

## Parameters

- `mapTemplate`: The current map template.

## See Also

### Panning the Map
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
- [func mapTemplate(CPMapTemplate, didUpdatePanGestureWithTranslation: CGPoint, velocity: CGPoint)](./maptemplate%28_,didupdatepangesturewithtranslation,velocity%29.md)
  Tells the delegate that the pan gesture changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplatedidshowpanninginterface(_:))*