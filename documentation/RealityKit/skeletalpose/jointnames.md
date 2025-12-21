# jointNames

**Framework**: RealityKit  
**Kind**: property

The names of the joints in the pose in specific order.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var jointNames: [String] { get set }
```

#### Discussion

Each joint name has a corresponding transformation value in [`jointTransforms`](skeletalpose/jointtransforms.md) at the same index.

Updates of the value results in resizing or reordering of the pose’s [`jointTransforms`](skeletalpose/jointtransforms.md) to match. New joint names add identity transformations at the matching indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalpose/jointnames)*