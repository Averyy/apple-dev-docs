# mapTemplateWillDismissPanningInterface(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the panning interface will disappear from the map.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplateWillDismissPanningInterface(_ mapTemplate: CPMapTemplate)
```

```objc
- (void) mapTemplateWillDismissPanningInterface:(CPMapTemplate *) mapTemplate;
```

## Parameters

- `mapTemplate`: The current map template.

## See Also

### Showing the panning interface
- [func mapTemplateDidShowPanningInterface(CPMapTemplate)](./maptemplatedidshowpanninginterface%28_%29.md)
  Tells the delegate that the panning interface is visible on the map.
- [func mapTemplateDidDismissPanningInterface(CPMapTemplate)](./maptemplatediddismisspanninginterface%28_%29.md)
  Tells the delegate that the panning interface is no longer visible on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplatewilldismisspanninginterface(_:))*