# targetAlignment

**Framework**: ARKit  
**Kind**: property

The alignment of the plane that the ray intersected.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var targetAlignment: ARRaycastQuery.TargetAlignment { get }
```

## See Also

- [var worldTransform: simd_float4x4](arraycastresult/worldtransform.md)
  The position, rotation, and scale, of the ray’s intersection with the target.
- [var anchor: ARAnchor?](arraycastresult/anchor.md)
  The anchor for the plane that the ray intersected.
- [var target: ARRaycastQuery.Target](arraycastresult/target.md)
  The type of surface that the ray intersects.
- [ARRaycastQuery.Target](arraycastquery/target-swift.enum.md)
  The types of surface you allow a raycast to intersect with.
- [ARRaycastQuery.TargetAlignment](arraycastquery/targetalignment-swift.enum.md)
  A specification that indicates a target’s alignment with respect to gravity


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arraycastresult/targetalignment)*