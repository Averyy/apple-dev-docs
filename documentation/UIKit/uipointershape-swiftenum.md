# UIPointerShape

**Framework**: UIKit  
**Kind**: enum

An object that defines the shape of custom pointers.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
enum UIPointerShape
```

#### Overview

If the desired pointer shape can be expressed as a rounded rectangle, use [`UIPointerShape.roundedRect(_:radius:)`](uipointershape-swift.enum/roundedrect(_:radius:).md) for best results.

## Topics

### Specifying pointer shapes
- [UIPointerShape.horizontalBeam(length:)](uipointershape-swift.enum/horizontalbeam(length:).md)
  The pointer morphs into a horizontal beam using the specified length.
- [UIPointerShape.verticalBeam(length:)](uipointershape-swift.enum/verticalbeam(length:).md)
  The pointer morphs into a vertical beam using the specified length.
- [UIPointerShape.path(_:)](uipointershape-swift.enum/path(_:).md)
  The pointer morphs into the given Bézier path.
- [case roundedRect(CGRect, radius: CGFloat)](uipointershape-swift.enum/roundedrect(_:radius:).md)
  The pointer morphs into a rounded rectangle using the provided corner radius.
### Accessing corner radius
- [static let defaultCornerRadius: CGFloat](uipointershape-swift.enum/defaultcornerradius.md)
  The default corner radius for a pointer using a rounded rectangle.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)

## See Also

- [class UIPointerStyle](uipointerstyle.md)
  An object that defines the pointer shape and effect.
- [enum UIPointerEffect](uipointereffect-swift.enum.md)
  An effect that alters a view’s appearance when a pointer enters the current region.
- [class UIPointerAccessory](uipointeraccessory.md)
  Constants that describe accessories to display alongside the primary pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointershape-swift.enum)*