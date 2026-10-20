# targetAlignment

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The target’s alignment with respect to gravity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var targetAlignment: ARRaycastQuery.TargetAlignment { get }
```

```objc
@property (nonatomic, readonly) ARRaycastTargetAlignment targetAlignment;
```

#### Discussion

The available options are horizontal, vertical, or any.

## See Also

### Specifying the Target
- [var target: ARRaycastQuery.Target](./target-swift.property.md)
  A plane type that allows the raycast to terminate if it’s encountered.
- [ARRaycastQuery.Target](./target-swift.enum.md)
  The types of surface you allow a raycast to intersect with.
- [ARRaycastQuery.TargetAlignment](./targetalignment-swift.enum.md)
  A specification that indicates a target’s alignment with respect to gravity


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arraycastquery/targetalignment-swift.property)*