# isJointTracked(_:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Tells you whether ARKit tracks a joint at a particular index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
func isJointTracked(_ jointIndex: Int) -> Bool
```

```objc
- (BOOL) isJointTracked:(NSInteger) jointIndex;
```

#### Discussion

Use this function to determine which joints ARKit tracks using a particular index.

## See Also

### Getting Joint Information
- [var definition: ARSkeletonDefinition](./definition.md)
  The particular configuration of joints that define a body’s current state.
- [ARSkeleton.JointName](./jointname.md)
  A name identifier for a joint.
- [jointCount](./jointcount.md)
  The skeleton’s total number of joints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton/isjointtracked(_:))*