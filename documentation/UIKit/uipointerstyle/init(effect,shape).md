# init(effect:shape:)

**Framework**: UIKit  
**Kind**: init

Applies the provided content effect and pointer shape to the current region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(effect: UIPointerEffect, shape: UIPointerShape? = nil)
```

## Parameters

- `effect`: The [`UIPointerEffect`](uipointereffect-swift.enum.md) to apply to the region.
- `shape`: The [`UIPointerShape`](uipointershape-swift.enum.md) to use, defaults to `nil`.

## See Also

- [convenience init(shape: UIPointerShape, constrainedAxes: UIAxis)](uipointerstyle/init(shape:constrainedaxes:).md)
  Morphs the pointer into the provided shape when hovering over the current region.
- [class func hidden() -> Self](uipointerstyle/hidden.md)
  Hides the pointer when it moves over the current region.
- [class func system() -> Self](uipointerstyle/system.md)
  Morphs the pointer into a default system-style pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerstyle/init(effect:shape:))*