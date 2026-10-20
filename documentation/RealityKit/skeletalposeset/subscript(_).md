# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the pose at the specified index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
subscript(index: SkeletalPoseSet.Index) -> SkeletalPoseSet.Element { get set }
```

**Other overloads**:

```swift
subscript(poseID: SkeletalPose.ID) -> SkeletalPoseSet.Element? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalposeset/subscript(_:))*