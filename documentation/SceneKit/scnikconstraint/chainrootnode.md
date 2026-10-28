# chainRootNode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The parent node of the hierarchy affected by the constraint.

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
var chainRootNode: SCNNode { get }
```

```objc
@property (nonatomic, readonly) SCNNode * chainRootNode;
```

## Discussion

The root node is the highest node in the hierarchy moved by the constraint. For example, a robot arm may have two arm segments and a hand connected to a body. The upper arm is a child node of the body, the lower arm is a child node of the upper arm, and the hand is a child node of the lower arm. In this case, the upper arm is the chain root node, because the body should not move to follow the hand.

## See Also

### Adjusting the Constraint’s Limits of Motion
- [func maxAllowedRotationAngle(forJoint: SCNNode) -> CGFloat](./maxallowedrotationangle%28forjoint%29.md)
  Returns the rotation limit, in degrees, for the specified node.
- [func setMaxAllowedRotationAngle(CGFloat, forJoint: SCNNode)](./setmaxallowedrotationangle%28_,forjoint%29.md)
  Sets the rotation limit, in degrees, for the specified node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnikconstraint/chainrootnode)*