# joint(_:)

**Framework**: ARKit  
**Kind**: method

Retrieves a hand joint based on the joint name you specify.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func joint(_ named: HandSkeleton.JointName) -> HandSkeleton.Joint
```

#### Return Value

A hand joint referred to by the `named` parameter.

## Parameters

- `named`: The name of the hand joint to retrieve.

## See Also

- [HandSkeleton.Joint](handskeleton/joint.md)
  The name and position of an individual hand joint.
- [HandSkeleton.JointName](handskeleton/jointname.md)
  The names of different hand joints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handskeleton/joint(_:))*