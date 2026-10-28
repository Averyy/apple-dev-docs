# UIPointerShape

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that defines the shape of custom pointers.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```objc
@interface UIPointerShape : NSObject
```

## Overview

If the desired pointer shape can be expressed as a rounded rectangle, use either [`shapeWithRoundedRect:`](./uipointershape-c.class/shapewithroundedrect_.md) or [`shapeWithRoundedRect:cornerRadius:`](./uipointershape-c.class/shapewithroundedrect_cornerradius_.md) for best results.

> **Note**:  If used alongside a content effect, this rectangle must be in the view coordinate space of the [`preview`](./uipointereffect-swift.enum/preview.md). Otherwise, it’s centered about the pointer’s current location, and the rectangle’s origin is interpreted as an offset.

## Topics

### Specifying pointer shapes
- [+ beamWithPreferredLength:axis:](./uipointershape-c.class/beamwithpreferredlength_axis_.md)
  Morphs the pointer into a vertical or horizontal beam.
- [+ shapeWithPath:](./uipointershape-c.class/shapewithpath_.md)
  Morphs the pointer into the given Bézier path.
- [+ shapeWithRoundedRect:](./uipointershape-c.class/shapewithroundedrect_.md)
  Morphs the pointer into a rounded rectangle using the default corner radius.
- [+ shapeWithRoundedRect:cornerRadius:](./uipointershape-c.class/shapewithroundedrect_cornerradius_.md)
  Morphs the pointer into a rounded rectangle using the provided corner radius.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Pointer styles
- [class UIPointerStyle](./uipointerstyle.md)
  An object that defines the pointer shape and effect.
- [UIPointerEffect](./uipointereffect-c.class.md)
  An effect that alters a view’s appearance when a pointer enters the current region.
- [class UIPointerAccessory](./uipointeraccessory.md)
  Constants that describe accessories to display alongside the primary pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointershape-c.class)*