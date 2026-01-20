# CIFlashTransition

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a flash transition filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIFlashTransition : CITransitionFilter
```

## Topics

### Instance Properties
- [var center: CGPoint](ciflashtransition/center.md)
  The x and y position to use as the center of the effect.
- [var color: CIColor](ciflashtransition/color.md)
  The color of the light rays emanating from the flash.
- [var extent: CGRect](ciflashtransition/extent.md)
  The extent of the flash.
- [var fadeThreshold: Float](ciflashtransition/fadethreshold.md)
  The amount of fade between the flash and the target image.
- [var maxStriationRadius: Float](ciflashtransition/maxstriationradius.md)
  The radius of the light rays emanating from the flash.
- [var striationContrast: Float](ciflashtransition/striationcontrast.md)
  The contrast of the light rays emanating from the flash.
- [var striationStrength: Float](ciflashtransition/striationstrength.md)
  The strength of the light rays emanating from the flash.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func flashTransition() -> any CIFilter & CIFlashTransition](cifilter-swift.class/flashtransition.md)
  Creates a flash of light to transition between two images.
- [protocol CITransitionFilter](citransitionfilter.md)
  The properties you use to configure a transition filter.
- [protocol CIBarsSwipeTransition](cibarsswipetransition.md)
  The properties you use to configure a bars swipe transition filter.
- [protocol CIAccordionFoldTransition](ciaccordionfoldtransition.md)
  The properties you use to configure an accordion fold transition filter.
- [protocol CICopyMachineTransition](cicopymachinetransition.md)
  The properties you use to configure a copy machine transition filter.
- [protocol CIDisintegrateWithMaskTransition](cidisintegratewithmasktransition.md)
  The properties you use to configure a disintegrate-with-mask transition filter.
- [protocol CIDissolveTransition](cidissolvetransition.md)
  The properties you use to configure a dissolve transition filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciflashtransition)*