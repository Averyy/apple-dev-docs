# ObjectCaptureSession.Tracking.limited(reason:)

**Framework**: RealityKit  
**Kind**: case

Tracking is available but its quality is degraded. The ARKit coaching overlay will appear when [`cameraTracking`](objectcapturesession/cameratracking.md) enters this state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
case limited(reason: ObjectCaptureSession.Tracking.Reason)
```

## Parameters

- `reason`: Why tracking is currently degraded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/tracking/limited(reason:))*