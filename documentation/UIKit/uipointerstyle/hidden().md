# hidden()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Hides the pointer when it moves over the current region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
class func hidden() -> Self
```

```objc
+ (instancetype) hiddenPointerStyle;
```

## See Also

### Creating a pointer style
- [convenience init(effect: UIPointerEffect, shape: UIPointerShape?)](./init%28effect,shape%29.md)
  Applies the provided content effect and pointer shape to the current region.
- [convenience init(shape: UIPointerShape, constrainedAxes: UIAxis)](./init%28shape,constrainedaxes%29.md)
  Morphs the pointer into the provided shape when hovering over the current region.
- [class func system() -> Self](./system%28%29.md)
  Morphs the pointer into a default system-style pointer.
- [+ styleWithEffect:shape:](./stylewitheffect_shape_.md)
  Applies the provided content effect and pointer shape to the current region.
- [+ styleWithShape:constrainedAxes:](./stylewithshape_constrainedaxes_.md)
  Morphs the pointer into the provided shape when it moves over the current region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerstyle/hidden())*