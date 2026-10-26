# jointCount

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The skeleton’s total number of joints.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var jointCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger jointCount;
```

## See Also

### Getting Joint Information
- [var jointNames: [String]](./jointnames.md)
  A collection of unique joint names.
- [func index(for: ARSkeleton.JointName) -> Int](./index%28for%29.md)
  Returns the index for a given joint identifier.
- [var parentIndices: [Int]](./parentindices-u2u9.md)
  The parent index for each joint.
- [- indexForJointName:](./indexforjointname_.md)
  Returns the index for a given joint identifier.
- [parentIndices](./parentindices-82iw2.md)
  The parent index for each joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeletondefinition/jointcount)*