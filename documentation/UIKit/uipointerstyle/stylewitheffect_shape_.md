# styleWithEffect:shape:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Applies the provided content effect and pointer shape to the current region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) styleWithEffect:(UIPointerEffect *) effect shape:(UIPointerShape *) shape;
```

## Parameters

- `effect`: The [`UIPointerEffect`](../uipointereffect-swift.enum.md) to apply to the region.
- `shape`: The [`UIPointerShape`](../uipointershape-swift.enum.md) to apply to the region.

## See Also

### Creating a pointer style
- [+ styleWithShape:constrainedAxes:](./stylewithshape_constrainedaxes_.md)
  Morphs the pointer into the provided shape when it moves over the current region.
- [class func hidden() -> Self](./hidden%28%29.md)
  Hides the pointer when it moves over the current region.
- [class func system() -> Self](./system%28%29.md)
  Morphs the pointer into a default system-style pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerstyle/stylewitheffect:shape:)*