# init(tracking:sceneUnderstanding:camera:)

**Framework**: RealityKit  
**Kind**: init

Creates a configuration with anchor capabilities, scene-understanding capabilities, and camera feeds.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
init(tracking anchorCapabilities: Set<SpatialTrackingSession.Configuration.AnchorCapability> = [], sceneUnderstanding: Set<SpatialTrackingSession.Configuration.SceneUnderstandingCapability> = [], camera: SpatialTrackingSession.Configuration.Camera = .back)
```

## Parameters

- `anchorCapabilities`: The set of anchor capabilities   to run with a  .
- `sceneUnderstanding`: The set of scene-understanding capabilities   to run with a  .
- `camera`: The camera feed to run with a  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/configuration/init(tracking:sceneunderstanding:camera:))*