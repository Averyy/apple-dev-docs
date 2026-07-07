# init(session:cameraFeedOverlay:)

**Framework**: RealityKit  
**Kind**: init

Renders the current state of the provided session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
nonisolated
init(session: ObjectCaptureSession, @ViewBuilder cameraFeedOverlay: () -> Overlay)
```

## Parameters

- `cameraFeedOverlay`: A view that appears on top of the camera feed and below the point cloud view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcaptureview/init(session:camerafeedoverlay:))*