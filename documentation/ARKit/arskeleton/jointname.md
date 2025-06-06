# ARSkeleton.JointName

**Framework**: ARKit  
**Kind**: struct

A name identifier for a joint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct JointName
```

#### Discussion

Use this class to access information about a named joint, such as its index in a skeleton’s array of joints, or its position on the screen or in the physical environment.

When you’re tracking a body in 2D space, you get the screen-space position of a named joint by using the [`landmark(for:)`](arskeleton2d/landmark(for:).md) function.

When you’re tracking a body in 3D space, you get a named joint’s position in either local or model space by using the [`localTransform(for:)`](arskeleton3d/localtransform(for:).md) or [`modelTransform(for:)`](arskeleton3d/modeltransform(for:).md) functions, respectively.

## Topics

### Creating a Joint Name
- [init(rawValue: String)](arskeleton/jointname/init(rawvalue:).md)
  Creates a new joint name.
- [init?(VNRecognizedPointKey)](arskeleton/jointname/init(_:).md)
  Returns a joint name that corresponds to a key point defined in a human body pose.
- [struct VNRecognizedPointKey](../Vision/VNRecognizedPointKey.md)
  The data type for all recognized point keys.
### Identifying Joints
- [static let root: ARSkeleton.JointName](arskeleton/jointname/root.md)
  A skeletal joint that’s the root of all other joints.
- [static let head: ARSkeleton.JointName](arskeleton/jointname/head.md)
  A skeletal joint that ARKit tracks representing the head.
- [static let leftFoot: ARSkeleton.JointName](arskeleton/jointname/leftfoot.md)
  A skeletal joint that ARKit tracks representing the left foot.
- [static let leftHand: ARSkeleton.JointName](arskeleton/jointname/lefthand.md)
  A skeletal joint that ARKit tracks representing the left hand.
- [static let leftShoulder: ARSkeleton.JointName](arskeleton/jointname/leftshoulder.md)
  A skeletal joint that ARKit tracks representing the left shoulder.
- [static let rightFoot: ARSkeleton.JointName](arskeleton/jointname/rightfoot.md)
  A skeletal joint that ARKit tracks representing the right foot.
- [static let rightHand: ARSkeleton.JointName](arskeleton/jointname/righthand.md)
  A skeletal joint that ARKit tracks representing the right hand.
- [static let rightShoulder: ARSkeleton.JointName](arskeleton/jointname/rightshoulder.md)
  A skeletal joint that ARKit tracks representing the right shoulder.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var definition: ARSkeletonDefinition](arskeleton/definition.md)
  The particular configuration of joints that define a body’s current state.
- [func isJointTracked(Int) -> Bool](arskeleton/isjointtracked(_:).md)
  Tells you whether ARKit tracks a joint at a particular index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton/jointname)*