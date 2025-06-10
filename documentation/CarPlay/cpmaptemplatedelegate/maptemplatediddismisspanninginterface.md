# mapTemplateDidDismissPanningInterface(_:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that the panning interface is no longer visible on the map.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func mapTemplateDidDismissPanningInterface(_ mapTemplate: CPMapTemplate)
```

## Parameters

- `mapTemplate`: The current map template.

## See Also

- [func mapTemplateDidShowPanningInterface(CPMapTemplate)](cpmaptemplatedelegate/maptemplatedidshowpanninginterface(_:).md)
  Tells the delegate that the panning interface is visible on the map.
- [func mapTemplateWillDismissPanningInterface(CPMapTemplate)](cpmaptemplatedelegate/maptemplatewilldismisspanninginterface(_:).md)
  Tells the delegate that the panning interface will disappear from the map.
- [func mapTemplateDidBeginPanGesture(CPMapTemplate)](cpmaptemplatedelegate/maptemplatedidbeginpangesture(_:).md)
  Tells the delegate that the pan gesture has started.
- [func mapTemplate(CPMapTemplate, panBeganWith: CPMapTemplate.PanDirection)](cpmaptemplatedelegate/maptemplate(_:panbeganwith:).md)
  Tells the delegate that the user is starting to pan the map.
- [func mapTemplate(CPMapTemplate, panWith: CPMapTemplate.PanDirection)](cpmaptemplatedelegate/maptemplate(_:panwith:).md)
  Tells the delegate that the user is panning in a certain direction on the map.
- [func mapTemplate(CPMapTemplate, panEndedWith: CPMapTemplate.PanDirection)](cpmaptemplatedelegate/maptemplate(_:panendedwith:).md)
  Tells the delegate that the user stopped panning the map.
- [CPMapTemplate.PanDirection](cpmaptemplate/pandirection.md)
  The directions a user can pan (or move) a map displayed on the CarPlay screen.
- [func mapTemplate(CPMapTemplate, didEndPanGestureWithVelocity: CGPoint)](cpmaptemplatedelegate/maptemplate(_:didendpangesturewithvelocity:).md)
  Tells the delegate that the pan gesture ended with the specified velocity.
- [func mapTemplate(CPMapTemplate, didUpdatePanGestureWithTranslation: CGPoint, velocity: CGPoint)](cpmaptemplatedelegate/maptemplate(_:didupdatepangesturewithtranslation:velocity:).md)
  Tells the delegate that the pan gesture changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplatediddismisspanninginterface(_:))*