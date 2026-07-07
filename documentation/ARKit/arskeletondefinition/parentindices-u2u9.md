# parentIndices

**Framework**: ARKit  
**Kind**: property

The parent index for each joint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
@nonobjc
var parentIndices: [Int] { get }
```

#### Discussion

This property may be used to identify the hierarchical dependency between joints. If a line is drawn for every joint and its parent joint, the result is a visualization of the underlying skeleton. The joint with no parent is denoted as the root joint. The root joint’s parent index is -1.

## See Also

- [var jointNames: [String]](arskeletondefinition/jointnames.md)
  A collection of unique joint names.
- [var jointCount: Int](arskeletondefinition/jointcount.md)
  The skeleton’s total number of joints.
- [func index(for: ARSkeleton.JointName) -> Int](arskeletondefinition/index(for:).md)
  Returns the index for a given joint identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeletondefinition/parentindices-u2u9)*