# ARRaycastQuery.TargetAlignment

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

A specification that indicates a target’s alignment with respect to gravity

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
enum TargetAlignment
```

```c
enum ARRaycastTargetAlignment : NSInteger;
```

## Discussion

A raycast ignores potential targets with an alignment different than the one you specify in the raycast query.

## Topics

### Enumeration Cases
- [ARRaycastQuery.TargetAlignment.any](./targetalignment-swift.enum/any.md)
  The case that indicates a target may be aligned in any way with respect to gravity.
- [ARRaycastQuery.TargetAlignment.horizontal](./targetalignment-swift.enum/horizontal.md)
  The case that indicates a target is aligned horizontally with respect to gravity.
- [ARRaycastQuery.TargetAlignment.vertical](./targetalignment-swift.enum/vertical.md)
  The case that indicates a target is aligned vertically with respect to gravity.
### Initializers
- [init?(rawValue: Int)](./targetalignment-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the Target
- [var target: ARRaycastQuery.Target](./target-swift.property.md)
  A plane type that allows the raycast to terminate if it’s encountered.
- [ARRaycastQuery.Target](./target-swift.enum.md)
  The types of surface you allow a raycast to intersect with.
- [var targetAlignment: ARRaycastQuery.TargetAlignment](./targetalignment-swift.property.md)
  The target’s alignment with respect to gravity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arraycastquery/targetalignment-swift.enum)*