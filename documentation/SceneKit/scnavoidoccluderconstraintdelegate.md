# SCNAvoidOccluderConstraintDelegate

**Framework**: SceneKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
protocol SCNAvoidOccluderConstraintDelegate : NSObjectProtocol
```

```objc
@protocol SCNAvoidOccluderConstraintDelegate <NSObject>
```

## Topics

### Instance Methods
- [func avoidOccluderConstraint(SCNAvoidOccluderConstraint, didAvoidOccluder: SCNNode, for: SCNNode)](./scnavoidoccluderconstraintdelegate/avoidoccluderconstraint%28_,didavoidoccluder,for%29.md)
- [func avoidOccluderConstraint(SCNAvoidOccluderConstraint, shouldAvoidOccluder: SCNNode, for: SCNNode) -> Bool](./scnavoidoccluderconstraintdelegate/avoidoccluderconstraint%28_,shouldavoidoccluder,for%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring Constraint Behavior
- [var bias: CGFloat](./scnavoidoccluderconstraint/bias.md)
- [var occluderCategoryBitMask: Int](./scnavoidoccluderconstraint/occludercategorybitmask.md)
- [var target: SCNNode?](./scnavoidoccluderconstraint/target.md)
- [var delegate: any SCNAvoidOccluderConstraintDelegate](./scnavoidoccluderconstraint/delegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnavoidoccluderconstraintdelegate)*