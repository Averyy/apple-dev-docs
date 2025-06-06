# SCNAvoidOccluderConstraintDelegate

**Framework**: SceneKit  
**Kind**: protocol

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
protocol SCNAvoidOccluderConstraintDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func avoidOccluderConstraint(SCNAvoidOccluderConstraint, didAvoidOccluder: SCNNode, for: SCNNode)](scnavoidoccluderconstraintdelegate/avoidoccluderconstraint(_:didavoidoccluder:for:).md)
- [func avoidOccluderConstraint(SCNAvoidOccluderConstraint, shouldAvoidOccluder: SCNNode, for: SCNNode) -> Bool](scnavoidoccluderconstraintdelegate/avoidoccluderconstraint(_:shouldavoidoccluder:for:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var bias: CGFloat](scnavoidoccluderconstraint/bias.md)
- [var occluderCategoryBitMask: Int](scnavoidoccluderconstraint/occludercategorybitmask.md)
- [var target: SCNNode?](scnavoidoccluderconstraint/target.md)
- [var delegate: any SCNAvoidOccluderConstraintDelegate](scnavoidoccluderconstraint/delegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnavoidoccluderconstraintdelegate)*