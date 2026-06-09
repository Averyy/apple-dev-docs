# init(named:rootJoint:)

**Framework**: RealityKit  
**Kind**: init

Creates an IK rig from a joint hierarchy.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(named name: String, rootJoint: SkeletonResource.Joint) throws
```

#### Discussion

> **Note**: If the joint hierarchy contains invalid data.

## Parameters

- `name`: The name to associate with the rig.
- `rootJoint`: The root joint of the skeleton hierarchy to derive the rig from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/init(named:rootjoint:))*