# run(_:session:arConfiguration:)

**Framework**: RealityKit  
**Kind**: method

Runs the spatial tracking session with a spatial tracking configuration, an AR session, and an AR configuration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@discardableResult
@MainActor final func run(_ configuration: SpatialTrackingSession.Configuration, session: ARSession, arConfiguration: ARConfiguration) async -> SpatialTrackingSession.UnavailableCapabilities?
```

#### Return Value

The unavailable capabilities based on the hardware and the user authorization.

#### Discussion

You manage and run the [`ARSession`](https://developer.apple.com/documentation/ARKit/ARSession) for the `SpatialTrackingSession`.

## Parameters

- `configuration`: An object that configures the AR data that RealityKit uses in the spatial tracking session.
- `session`: An object that coordinates the major processes that ARKit performs on your behalf to create an augmented reality experience.
- `arConfiguration`: An object that defines motion and scene tracking behaviors for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/run(_:session:arconfiguration:))*