# indexForJointName:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the index for a given joint identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```objc
- (NSUInteger) indexForJointName:(ARSkeletonJointName) jointName;
```

## Discussion

This function returns `NSNotFound` if an invalid joint name is passed in.

## See Also

### Getting Joint Information
- [var jointNames: [String]](./jointnames.md)
  A collection of unique joint names.
- [var jointCount: Int](./jointcount.md)
  The skeleton’s total number of joints.
- [parentIndices](./parentindices-82iw2.md)
  The parent index for each joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeletondefinition/indexforjointname:)*