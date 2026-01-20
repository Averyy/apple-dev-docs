# CICopyMachineTransition

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a copy machine transition filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CICopyMachineTransition : CITransitionFilter
```

## Topics

### Instance Properties
- [var angle: Float](cicopymachinetransition/angle.md)
  The angle of the copier light.
- [var color: CIColor](cicopymachinetransition/color.md)
  The color of the copier light.
- [var extent: CGRect](cicopymachinetransition/extent.md)
  A rectangle that defines the extent of the effect.
- [var opacity: Float](cicopymachinetransition/opacity.md)
  The opacity of the copier light.
- [var width: Float](cicopymachinetransition/width.md)
  The width of the copier light.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func copyMachineTransition() -> any CIFilter & CICopyMachineTransition](cifilter-swift.class/copymachinetransition.md)
  Simulates the effect of a copy machine scanner light to transiton between two images.
- [protocol CITransitionFilter](citransitionfilter.md)
  The properties you use to configure a transition filter.
- [protocol CIBarsSwipeTransition](cibarsswipetransition.md)
  The properties you use to configure a bars swipe transition filter.
- [protocol CIAccordionFoldTransition](ciaccordionfoldtransition.md)
  The properties you use to configure an accordion fold transition filter.
- [protocol CIDisintegrateWithMaskTransition](cidisintegratewithmasktransition.md)
  The properties you use to configure a disintegrate-with-mask transition filter.
- [protocol CIDissolveTransition](cidissolvetransition.md)
  The properties you use to configure a dissolve transition filter.
- [protocol CIFlashTransition](ciflashtransition.md)
  The properties you use to configure a flash transition filter.
- [protocol CIModTransition](cimodtransition.md)
  The properties you use to configure a mod transition filter.
- [protocol CIPageCurlTransition](cipagecurltransition.md)
  The properties you use to configure a page curl transition filter.
- [protocol CIPageCurlWithShadowTransition](cipagecurlwithshadowtransition.md)
  The properties you use to configure a page-curl-with-shadow transition filter.
- [protocol CIRippleTransition](cirippletransition.md)
  The properties you use to configure a ripple transition filter.
- [protocol CISwipeTransition](ciswipetransition.md)
  The properties you use to configure a swipe transition filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicopymachinetransition)*