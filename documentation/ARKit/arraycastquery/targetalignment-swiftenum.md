# ARRaycastQuery.TargetAlignment

**Framework**: ARKit  
**Kind**: enum

A specification that indicates a target’s alignment with respect to gravity

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum TargetAlignment
```

#### Discussion

A raycast ignores potential targets with an alignment different than the one you specify in the raycast query.

## Topics

### Enumeration Cases
- [ARRaycastQuery.TargetAlignment.any](arraycastquery/targetalignment-swift.enum/any.md)
  The case that indicates a target may be aligned in any way with respect to gravity.
- [ARRaycastQuery.TargetAlignment.horizontal](arraycastquery/targetalignment-swift.enum/horizontal.md)
  The case that indicates a target is aligned horizontally with respect to gravity.
- [ARRaycastQuery.TargetAlignment.vertical](arraycastquery/targetalignment-swift.enum/vertical.md)
  The case that indicates a target is aligned vertically with respect to gravity.
### Initializers
- [init?(rawValue: Int)](arraycastquery/targetalignment-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var target: ARRaycastQuery.Target](arraycastquery/target-swift.property.md)
  A plane type that allows the raycast to terminate if it’s encountered.
- [ARRaycastQuery.Target](arraycastquery/target-swift.enum.md)
  The types of surface you allow a raycast to intersect with.
- [var targetAlignment: ARRaycastQuery.TargetAlignment](arraycastquery/targetalignment-swift.property.md)
  The target’s alignment with respect to gravity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arraycastquery/targetalignment-swift.enum)*