# index(for:)

**Framework**: ARKit  
**Kind**: method

Returns the index for a given joint identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
@nonobjc
func index(for jointName: ARSkeleton.JointName) -> Int
```

#### Discussion

This function returns `NSNotFound` if an invalid joint name is passed in.

## See Also

- [var jointNames: [String]](arskeletondefinition/jointnames.md)
  A collection of unique joint names.
- [var jointCount: Int](arskeletondefinition/jointcount.md)
  The skeleton’s total number of joints.
- [var parentIndices: [Int]](arskeletondefinition/parentindices-u2u9.md)
  The parent index for each joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeletondefinition/index(for:))*