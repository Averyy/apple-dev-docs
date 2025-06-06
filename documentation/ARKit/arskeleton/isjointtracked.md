# isJointTracked(_:)

**Framework**: ARKit  
**Kind**: method

Tells you whether ARKit tracks a joint at a particular index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func isJointTracked(_ jointIndex: Int) -> Bool
```

#### Discussion

Use this function to determine which joints ARKit tracks using a particular index.

## See Also

- [var definition: ARSkeletonDefinition](arskeleton/definition.md)
  The particular configuration of joints that define a body’s current state.
- [ARSkeleton.JointName](arskeleton/jointname.md)
  A name identifier for a joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton/isjointtracked(_:))*