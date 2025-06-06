# anchor

**Framework**: RealityKit  
**Kind**: property

A type that contains all unavailable anchor capabilities.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var anchor: Set<SpatialTrackingSession.Configuration.AnchorCapability> { get }
```

#### Discussion

The system marks certain anchor capabilities as unavailable if:

- The device running your app doesn’t support them.
- The person using the device doesn’t approve the corresponding ARKit authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialtrackingsession/unavailablecapabilities/anchor)*