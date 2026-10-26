# CPMapTemplate.PanDirection

**Framework**: CarPlay  
**Kind**: struct  
**Role**: Structure

The directions a user can pan (or move) a map displayed on the CarPlay screen.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct PanDirection
```

```c
enum CPPanDirection : NSInteger;
```

## Topics

### Pan Directions
- [static var down: CPMapTemplate.PanDirection](./pandirection/down.md)
  The user panned the map downward.
- [static var left: CPMapTemplate.PanDirection](./pandirection/left.md)
  The user panned the map to the left.
- [static var right: CPMapTemplate.PanDirection](./pandirection/right.md)
  The user panned the map to the right.
- [static var up: CPMapTemplate.PanDirection](./pandirection/up.md)
  The user panned the map upward.
- [CPPanDirectionNone](../cppandirection/cppandirectionnone.md)
### Initializers
- [init(rawValue: Int)](./pandirection/init%28rawvalue%29.md)
  Initializes a pan direction using the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Panning the Map
- [func mapTemplateDidShowPanningInterface(CPMapTemplate)](../cpmaptemplatedelegate/maptemplatedidshowpanninginterface%28_%29.md)
  Tells the delegate that the panning interface is visible on the map.
- [func mapTemplateWillDismissPanningInterface(CPMapTemplate)](../cpmaptemplatedelegate/maptemplatewilldismisspanninginterface%28_%29.md)
  Tells the delegate that the panning interface will disappear from the map.
- [func mapTemplateDidDismissPanningInterface(CPMapTemplate)](../cpmaptemplatedelegate/maptemplatediddismisspanninginterface%28_%29.md)
  Tells the delegate that the panning interface is no longer visible on the map.
- [func mapTemplateDidBeginPanGesture(CPMapTemplate)](../cpmaptemplatedelegate/maptemplatedidbeginpangesture%28_%29.md)
  Tells the delegate that the pan gesture has started.
- [func mapTemplate(CPMapTemplate, panBeganWith: CPMapTemplate.PanDirection)](../cpmaptemplatedelegate/maptemplate%28_,panbeganwith%29.md)
  Tells the delegate that the user is starting to pan the map.
- [func mapTemplate(CPMapTemplate, panWith: CPMapTemplate.PanDirection)](../cpmaptemplatedelegate/maptemplate%28_,panwith%29.md)
  Tells the delegate that the user is panning in a certain direction on the map.
- [func mapTemplate(CPMapTemplate, panEndedWith: CPMapTemplate.PanDirection)](../cpmaptemplatedelegate/maptemplate%28_,panendedwith%29.md)
  Tells the delegate that the user stopped panning the map.
- [func mapTemplate(CPMapTemplate, didEndPanGestureWithVelocity: CGPoint)](../cpmaptemplatedelegate/maptemplate%28_,didendpangesturewithvelocity%29.md)
  Tells the delegate that the pan gesture ended with the specified velocity.
- [func mapTemplate(CPMapTemplate, didUpdatePanGestureWithTranslation: CGPoint, velocity: CGPoint)](../cpmaptemplatedelegate/maptemplate%28_,didupdatepangesturewithtranslation,velocity%29.md)
  Tells the delegate that the pan gesture changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/pandirection)*