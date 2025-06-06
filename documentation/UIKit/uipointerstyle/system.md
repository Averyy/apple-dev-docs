# system()

**Framework**: UIKit  
**Kind**: method

Morphs the pointer into a default system-style pointer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func system() -> Self
```

#### Discussion

To display custom accessories alongside the default pointer, use this pointer style and assign your accessories to the [`accessories`](uipointerstyle/accessories.md) property.

## See Also

- [convenience init(effect: UIPointerEffect, shape: UIPointerShape?)](uipointerstyle/init(effect:shape:).md)
  Applies the provided content effect and pointer shape to the current region.
- [convenience init(shape: UIPointerShape, constrainedAxes: UIAxis)](uipointerstyle/init(shape:constrainedaxes:).md)
  Morphs the pointer into the provided shape when hovering over the current region.
- [class func hidden() -> Self](uipointerstyle/hidden.md)
  Hides the pointer when it moves over the current region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerstyle/system())*