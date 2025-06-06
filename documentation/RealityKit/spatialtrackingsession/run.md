# run(_:)

**Framework**: RealityKit  
**Kind**: method

Runs the spatial tracking session with the specified configuration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@discardableResult
final func run(_ spatialTrackingConfiguration: SpatialTrackingSession.Configuration) async -> SpatialTrackingSession.UnavailableCapabilities?
```

#### Return Value

The unavailable capabilities based on the hardware and the user authorization.

## Parameters

- `spatialTrackingConfiguration`: An object that configures the AR data that RealityKit uses in the spatial tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/run(_:))*