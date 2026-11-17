# index(for:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the index for a given joint identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
@nonobjc
func index(for jointName: ARSkeleton.JointName) -> Int
```

## Return Value

The index of the joint in the skeleton.

## Discussion

This function returns `NSNotFound` if an invalid joint name is passed in.

## Parameters

- `jointName`: The name of the joint.

## See Also

### Getting Joint Information
- [var jointNames: [String]](./jointnames.md)
  A collection of unique joint names.
- [var jointCount: Int](./jointcount.md)
  The skeleton’s total number of joints.
- [var parentIndices: [Int]](./parentindices-u2u9.md)
  The parent index for each joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeletondefinition/index(for:))*