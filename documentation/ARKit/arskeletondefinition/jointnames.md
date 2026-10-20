# jointNames

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A collection of unique joint names.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var jointNames: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * jointNames;
```

#### Discussion

Refer to this array to convert a joint index to a joint identifier.

## See Also

### Getting Joint Information
- [var jointCount: Int](./jointcount.md)
  The skeleton’s total number of joints.
- [func index(for: ARSkeleton.JointName) -> Int](./index%28for%29.md)
  Returns the index for a given joint identifier.
- [var parentIndices: [Int]](./parentindices-u2u9.md)
  The parent index for each joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeletondefinition/jointnames)*