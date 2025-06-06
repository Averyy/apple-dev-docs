# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript

Accesses the element with the specified identifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
subscript(poseID: SkeletalPose.ID) -> SkeletalPoseSet.Element? { get set }
```

#### Overview

If multiple poses share the same identifier, only the one with lowest index is accessed.

The update only has an effect if all of the following conditions are true:

- A pose with the provided identifier exists in the collection.
- The new value isn’t `nil`.
- The pose with the provided identifier contains the same number of elements for its [`jointTransforms`](skeletalpose/jointtransforms.md).

## Parameters

- `poseID`: The identifier of the requested pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalposeset/subscript(_:)-54jc0)*