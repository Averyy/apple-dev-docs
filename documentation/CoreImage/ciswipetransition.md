# CISwipeTransition

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a swipe transition filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CISwipeTransition : CITransitionFilter
```

## Topics

### Instance Properties
- [var angle: Float](ciswipetransition/angle.md)
  The angle of the swipe.
- [var color: CIColor](ciswipetransition/color.md)
  The color of the swipe.
- [var extent: CGRect](ciswipetransition/extent.md)
  The extent of the effect.
- [var opacity: Float](ciswipetransition/opacity.md)
  The opacity of the swipe.
- [var width: Float](ciswipetransition/width.md)
  The width of the swipe.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func swipeTransition() -> any CIFilter & CISwipeTransition](cifilter-swift.class/swipetransition.md)
  Gradually transitions from one image to another with a swiping motion.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciswipetransition)*