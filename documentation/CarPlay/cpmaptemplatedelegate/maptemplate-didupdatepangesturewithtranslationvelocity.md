# mapTemplate(_:didUpdatePanGestureWithTranslation:velocity:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that the pan gesture changed.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didUpdatePanGestureWithTranslation translation: CGPoint, velocity: CGPoint)
```

#### Discussion

CarPlay doesn’t call this method when connected to some CarPlay systems.

## Parameters

- `mapTemplate`: The current map template.
- `translation`: The updated translation point.
- `velocity`: The velocity of the pan gesture.

## See Also

- [func mapTemplateDidShowPanningInterface(CPMapTemplate)](cpmaptemplatedelegate/maptemplatedidshowpanninginterface(_:).md)
  Tells the delegate that the panning interface is visible on the map.
- [func mapTemplateWillDismissPanningInterface(CPMapTemplate)](cpmaptemplatedelegate/maptemplatewilldismisspanninginterface(_:).md)
  Tells the delegate that the panning interface will disappear from the map.
- [func mapTemplateDidDismissPanningInterface(CPMapTemplate)](cpmaptemplatedelegate/maptemplatediddismisspanninginterface(_:).md)
  Tells the delegate that the panning interface is no longer visible on the map.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didupdatepangesturewithtranslation:velocity:))*