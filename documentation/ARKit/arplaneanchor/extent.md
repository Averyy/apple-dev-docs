# extent

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The estimated width and length of the detected plane.

**Availability**:
- iOS 11.0+ - Deprecated in 16.0
- iPadOS 11.0+ - Deprecated in 16.0

## Declaration

```swift
var extent: simd_float3 { get }
```

```objc
@property (nonatomic, readonly) simd_float3 extent;
```

## Discussion

> ⚠️ **Warning**:  In iOS 16, use [`planeExtent`](./planeextent.md) instead.

The framework sets the x and z components to the width and length of the plane, respectively. The y-component is unused, with a constant value of `0`.

## See Also

### Dimensions
- [var center: simd_float3](./center.md)
  The center point of the plane relative to its anchor position.
- [var planeExtent: ARPlaneExtent](./planeextent.md)
  The estimated width, length, and y-axis rotation of the detected plane.
- [class ARPlaneExtent](../arplaneextent.md)
  The size and y-axis rotation of a detected plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/extent)*