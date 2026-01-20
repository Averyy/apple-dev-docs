# CIRippleTransition

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a ripple transition filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIRippleTransition : CITransitionFilter
```

## Topics

### Instance Properties
- [var center: CGPoint](cirippletransition/center.md)
  The x and y position to use as the center of the effect.
- [var extent: CGRect](cirippletransition/extent.md)
  A rectangle that defines the extent of the effect.
- [var scale: Float](cirippletransition/scale.md)
  A value that determines whether the ripple starts as a bulge (a higher value) or a dimple (a lower value).
- [var shadingImage: CIImage?](cirippletransition/shadingimage.md)
  An image that looks like a shaded sphere enclosed in a square.
- [var width: Float](cirippletransition/width.md)
  The width of the ripple.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func rippleTransition() -> any CIFilter & CIRippleTransition](cifilter-swift.class/rippletransition.md)
  Simulates a ripple in a pond to transiton from one image to another.
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
- [protocol CISwipeTransition](ciswipetransition.md)
  The properties you use to configure a swipe transition filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirippletransition)*