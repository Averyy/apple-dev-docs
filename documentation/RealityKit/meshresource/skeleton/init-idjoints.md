# init(id:joints:)

**Framework**: RealityKit  
**Kind**: init

Creates a skeleton from an array of joints.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(id: String, joints: [MeshResource.Skeleton.Joint])
```

#### Discussion

> ❗ **Important**: The order of joints in this array is significant; parents need to precede their children.

The order of joints in this array is significant; parents need to precede their children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/skeleton/init(id:joints:))*