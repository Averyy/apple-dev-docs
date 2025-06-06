# jointNames

**Framework**: ARKit  
**Kind**: property

A collection of unique joint names.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var jointNames: [String] { get }
```

#### Discussion

Refer to this array to convert a joint index to a joint identifier.

## See Also

- [var jointCount: Int](arskeletondefinition/jointcount.md)
  The skeleton’s total number of joints.
- [func index(for: ARSkeleton.JointName) -> Int](arskeletondefinition/index(for:).md)
  Returns the index for a given joint identifier.
- [var parentIndices: [Int]](arskeletondefinition/parentindices-u2u9.md)
  The parent index for each joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeletondefinition/jointnames)*