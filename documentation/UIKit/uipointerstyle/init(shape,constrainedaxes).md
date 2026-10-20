# init(shape:constrainedAxes:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Morphs the pointer into the provided shape when hovering over the current region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency convenience init(shape: UIPointerShape, constrainedAxes: UIAxis = [])
```

## Parameters

- `shape`: The [`UIPointerShape`](../uipointershape-swift.enum.md) to use, defaults to `nil`.
- `constrainedAxes`: An array of [`UIAxis`](../uiaxis.md) directions in which to constrain the pointer. The default is no constraints.

## See Also

### Creating a pointer style
- [convenience init(effect: UIPointerEffect, shape: UIPointerShape?)](./init%28effect,shape%29.md)
  Applies the provided content effect and pointer shape to the current region.
- [class func hidden() -> Self](./hidden%28%29.md)
  Hides the pointer when it moves over the current region.
- [class func system() -> Self](./system%28%29.md)
  Morphs the pointer into a default system-style pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerstyle/init(shape:constrainedaxes:))*