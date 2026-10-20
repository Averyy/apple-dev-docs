# target

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The type of surface that the ray intersects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var target: ARRaycastQuery.Target { get }
```

```objc
@property (nonatomic, assign, readonly) ARRaycastTarget target;
```

## See Also

### Identifying Results
- [var worldTransform: simd_float4x4](./worldtransform.md)
  The position, rotation, and scale, of the ray’s intersection with the target.
- [var anchor: ARAnchor?](./anchor.md)
  The anchor for the plane that the ray intersected.
- [ARRaycastQuery.Target](../arraycastquery/target-swift.enum.md)
  The types of surface you allow a raycast to intersect with.
- [var targetAlignment: ARRaycastQuery.TargetAlignment](./targetalignment.md)
  The alignment of the plane that the ray intersected.
- [ARRaycastQuery.TargetAlignment](../arraycastquery/targetalignment-swift.enum.md)
  A specification that indicates a target’s alignment with respect to gravity


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arraycastresult/target)*