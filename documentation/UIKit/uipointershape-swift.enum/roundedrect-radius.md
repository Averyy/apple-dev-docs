# UIPointerShape.roundedRect(_:radius:)

**Framework**: UIKit  
**Kind**: case

The pointer morphs into a rounded rectangle using the provided corner radius.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
case roundedRect(CGRect, radius: CGFloat = UIPointerShape.defaultCornerRadius)
```

#### Discussion

If you don’t specify a radius, the rounded rectangle uses the `defaultCornerRadius`.

> **Note**:  If used alongside a content effect, this rectangle must be in the view coordinate space of the [`preview`](uipointereffect-swift.enum/preview.md). Otherwise, it’s centered around the pointer’s current location, and the rectangle’s origin is interpreted as an offset.

 If used alongside a content effect, this rectangle must be in the view coordinate space of the [`preview`](uipointereffect-swift.enum/preview.md). Otherwise, it’s centered around the pointer’s current location, and the rectangle’s origin is interpreted as an offset.

## See Also

- [UIPointerShape.horizontalBeam(length:)](uipointershape-swift.enum/horizontalbeam(length:).md)
  The pointer morphs into a horizontal beam using the specified length.
- [UIPointerShape.verticalBeam(length:)](uipointershape-swift.enum/verticalbeam(length:).md)
  The pointer morphs into a vertical beam using the specified length.
- [UIPointerShape.path(_:)](uipointershape-swift.enum/path(_:).md)
  The pointer morphs into the given Bézier path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointershape-swift.enum/roundedrect(_:radius:))*