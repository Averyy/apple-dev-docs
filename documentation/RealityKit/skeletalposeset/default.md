# default

**Framework**: RealityKit  
**Kind**: property

Accesses the first skeletal pose.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var `default`: SkeletalPoseSet.Element? { get set }
```

#### Discussion

Equivalent to accessing [`jointNames`](hasmodel/jointnames.md) and [`jointTransforms`](hasmodel/jointtransforms.md) if used from an entity with a skeletal model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalposeset/default)*