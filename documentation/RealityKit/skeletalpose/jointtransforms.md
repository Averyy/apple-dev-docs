# jointTransforms

**Framework**: RealityKit  
**Kind**: property

The transformations of the joints in the pose.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var jointTransforms: JointTransforms
```

#### Discussion

Each joint transformation has a corresponding name in [`jointNames`](skeletalpose/jointnames.md) at the same index.

A new value with element count not matching the element count  of [`jointNames`](skeletalpose/jointnames.md) is accepted but invokes special handling when the [`SkeletalPosesComponent`](skeletalposescomponent.md) is set on an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalpose/jointtransforms)*