# CPMapTemplate.PanDirection

**Framework**: CarPlay  
**Kind**: struct

The directions a user can pan (or move) a map displayed on the CarPlay screen.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct PanDirection
```

## Topics

### Pan Directions
- [static var down: CPMapTemplate.PanDirection](cpmaptemplate/pandirection/down.md)
  The user panned the map downward.
- [static var left: CPMapTemplate.PanDirection](cpmaptemplate/pandirection/left.md)
  The user panned the map to the left.
- [static var right: CPMapTemplate.PanDirection](cpmaptemplate/pandirection/right.md)
  The user panned the map to the right.
- [static var up: CPMapTemplate.PanDirection](cpmaptemplate/pandirection/up.md)
  The user panned the map upward.
### Initializers
- [init(rawValue: Int)](cpmaptemplate/pandirection/init(rawvalue:).md)
  Initializes a pan direction using the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [func mapTemplate(CPMapTemplate, didEndPanGestureWithVelocity: CGPoint)](cpmaptemplatedelegate/maptemplate(_:didendpangesturewithvelocity:).md)
  Tells the delegate that the pan gesture ended with the specified velocity.
- [func mapTemplate(CPMapTemplate, didUpdatePanGestureWithTranslation: CGPoint, velocity: CGPoint)](cpmaptemplatedelegate/maptemplate(_:didupdatepangesturewithtranslation:velocity:).md)
  Tells the delegate that the pan gesture changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/pandirection)*