# init(originFromAnchorTransform:sharedWithNearbyParticipants:)

**Framework**: ARKit  
**Kind**: init

Initialize a world anchor with a transform and indicate if it should be shared with nearby participants.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(originFromAnchorTransform: simd_float4x4, sharedWithNearbyParticipants: Bool)
```

#### Discussion

> **Note**: - Nearby participants refer to participants that are nearby to the local participant in a SharePlay session.
- World anchors that are marked for sharing do not get persisted and their lifetime is limited to that of the SharePlay session.

## Parameters

- `originFromAnchorTransform`: The transform from the world anchor to the origin coordinate system.
- `sharedWithNearbyParticipants`: Indicate if the anchor should be shared with nearby participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldanchor/init(originfromanchortransform:sharedwithnearbyparticipants:))*