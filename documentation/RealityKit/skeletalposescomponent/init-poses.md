# init(poses:)

**Framework**: RealityKit  
**Kind**: init

Creates a component value with the provided poses.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(poses: [SkeletalPose])
```

#### Discussion

> ⚠️ **Warning**: When multiple poses share the same identifier, only the first one is accessible using its identifier.

When multiple poses share the same identifier, only the first one is accessible using its identifier.

## Parameters

- `poses`: The pose values, arranged in any order of your choosing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalposescomponent/init(poses:))*