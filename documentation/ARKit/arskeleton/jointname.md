# ARSkeleton.JointName

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

A name identifier for a joint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
struct JointName
```

```c
typedef NSString * ARSkeletonJointName;
```

#### Discussion

Use this class to access information about a named joint, such as its index in a skeleton’s array of joints, or its position on the screen or in the physical environment.

When you’re tracking a body in 2D space, you get the screen-space position of a named joint by using the [`landmark(for:)`](../arskeleton2d/landmark%28for%29.md) function.

When you’re tracking a body in 3D space, you get a named joint’s position in either local or model space by using the [`localTransform(for:)`](../arskeleton3d/localtransform%28for%29.md) or [`modelTransform(for:)`](../arskeleton3d/modeltransform%28for%29.md) functions, respectively.

## Topics

### Creating a Joint Name
- [init(rawValue: String)](./jointname/init%28rawvalue%29.md)
  Creates a new joint name.
- [init?(VNRecognizedPointKey)](./jointname/init%28_%29.md)
  Returns a joint name that corresponds to a key point defined in a human body pose.
- [struct VNRecognizedPointKey](../../Vision/vnrecognizedpointkey.md)
  The data type for all recognized point keys.
### Identifying Joints
- [static let root: ARSkeleton.JointName](./jointname/root.md)
  A skeletal joint that’s the root of all other joints.
- [static let head: ARSkeleton.JointName](./jointname/head.md)
  A skeletal joint that ARKit tracks representing the head.
- [static let leftFoot: ARSkeleton.JointName](./jointname/leftfoot.md)
  A skeletal joint that ARKit tracks representing the left foot.
- [static let leftHand: ARSkeleton.JointName](./jointname/lefthand.md)
  A skeletal joint that ARKit tracks representing the left hand.
- [static let leftShoulder: ARSkeleton.JointName](./jointname/leftshoulder.md)
  A skeletal joint that ARKit tracks representing the left shoulder.
- [static let rightFoot: ARSkeleton.JointName](./jointname/rightfoot.md)
  A skeletal joint that ARKit tracks representing the right foot.
- [static let rightHand: ARSkeleton.JointName](./jointname/righthand.md)
  A skeletal joint that ARKit tracks representing the right hand.
- [static let rightShoulder: ARSkeleton.JointName](./jointname/rightshoulder.md)
  A skeletal joint that ARKit tracks representing the right shoulder.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting Joint Information
- [var definition: ARSkeletonDefinition](./definition.md)
  The particular configuration of joints that define a body’s current state.
- [func isJointTracked(Int) -> Bool](./isjointtracked%28_%29.md)
  Tells you whether ARKit tracks a joint at a particular index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton/jointname)*