# PhotogrammetrySession.Request.poses

**Framework**: RealityKit  
**Kind**: case

Requests the estimated pose of the camera in each shot (relative to the common estimated coordinate system shared with the `.bounds` request).

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
case poses
```

#### Discussion

Once initial photogrammetric calculations are complete, a [`PhotogrammetrySession.Poses`](photogrammetrysession/poses.md) object will be returned with the estimated camera pose for each sample that was used in the reconstruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/request/poses)*