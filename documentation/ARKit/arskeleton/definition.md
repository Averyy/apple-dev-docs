# definition

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The particular configuration of joints that define a body’s current state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var definition: ARSkeletonDefinition { get }
```

```objc
@property (nonatomic, readonly) ARSkeletonDefinition * definition;
```

## See Also

### Getting Joint Information
- [func isJointTracked(Int) -> Bool](./isjointtracked%28_%29.md)
  Tells you whether ARKit tracks a joint at a particular index.
- [ARSkeleton.JointName](./jointname.md)
  A name identifier for a joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton/definition)*