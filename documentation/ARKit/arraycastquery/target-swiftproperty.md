# target

**Framework**: ARKit  
**Kind**: property

A plane type that allows the raycast to terminate if it’s encountered.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var target: ARRaycastQuery.Target { get }
```

#### Discussion

The available target types are plane, infinite plane, and estimated plane.

## See Also

- [ARRaycastQuery.Target](arraycastquery/target-swift.enum.md)
  The types of surface you allow a raycast to intersect with.
- [var targetAlignment: ARRaycastQuery.TargetAlignment](arraycastquery/targetalignment-swift.property.md)
  The target’s alignment with respect to gravity.
- [ARRaycastQuery.TargetAlignment](arraycastquery/targetalignment-swift.enum.md)
  A specification that indicates a target’s alignment with respect to gravity


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arraycastquery/target-swift.property)*