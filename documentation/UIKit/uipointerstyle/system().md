# system()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Morphs the pointer into a default system-style pointer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
class func system() -> Self
```

```objc
+ (instancetype) systemPointerStyle;
```

#### Discussion

To display custom accessories alongside the default pointer, use this pointer style and assign your accessories to the [`accessories`](./accessories.md) property.

## See Also

### Creating a pointer style
- [convenience init(effect: UIPointerEffect, shape: UIPointerShape?)](./init%28effect,shape%29.md)
  Applies the provided content effect and pointer shape to the current region.
- [convenience init(shape: UIPointerShape, constrainedAxes: UIAxis)](./init%28shape,constrainedaxes%29.md)
  Morphs the pointer into the provided shape when hovering over the current region.
- [class func hidden() -> Self](./hidden%28%29.md)
  Hides the pointer when it moves over the current region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerstyle/system())*