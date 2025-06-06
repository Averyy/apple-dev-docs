# init(shape:constrainedAxes:)

**Framework**: UIKit  
**Kind**: init

Morphs the pointer into the provided shape when hovering over the current region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(shape: UIPointerShape, constrainedAxes: UIAxis = [])
```

## Parameters

- `shape`: The   to use, defaults to  .
- `constrainedAxes`: An array of   directions in which to constrain the pointer. The default is no constraints.

## See Also

- [convenience init(effect: UIPointerEffect, shape: UIPointerShape?)](uipointerstyle/init(effect:shape:).md)
  Applies the provided content effect and pointer shape to the current region.
- [class func hidden() -> Self](uipointerstyle/hidden.md)
  Hides the pointer when it moves over the current region.
- [class func system() -> Self](uipointerstyle/system.md)
  Morphs the pointer into a default system-style pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerstyle/init(shape:constrainedaxes:))*