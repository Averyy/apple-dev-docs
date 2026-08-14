# setARSession(_:)

**Framework**: Nearby Interaction  
**Kind**: method

Provides the framework with an existing AR session to use for Camera Assistance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func setARSession(_ session: ARSession)
```

#### Discussion

Set the [`isCameraAssistanceEnabled`](ninearbypeerconfiguration/iscameraassistanceenabled.md) flag to `true` before calling this function. If you enable the flag and run a nearby-interaction session without calling [`setARSession(_:)`](nisession/setarsession(_:).md), the framework creates an internal [`ARSession`](https://developer.apple.com/documentation/arkit/arsession) instance to which the app has no access.

## Parameters

- `session`: An existing AR session configured as follows: - A world-tracking configuration ([`ARWorldTrackingConfiguration`](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration)) with [`worldAlignment`](https://developer.apple.com/documentation/arkit/arconfiguration/worldalignment-swift.property) `=` [`ARConfiguration.WorldAlignment.gravity`](https://developer.apple.com/documentation/arkit/arconfiguration/worldalignment-swift.enum/gravity), [`isCollaborationEnabled`](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/iscollaborationenabled) `=` `false`, [`userFaceTrackingEnabled`](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/userfacetrackingenabled) `=` `false`, and [`initialWorldMap`](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/initialworldmap) `=` `nil`.
- A delegate that returns `false` for [`sessionShouldAttemptRelocalization(_:)`](https://developer.apple.com/documentation/arkit/arsessionobserver/sessionshouldattemptrelocalization(_:)).

## See Also

- [func worldTransform(for: NINearbyObject) -> simd_float4x4?](nisession/worldtransform(for:).md)
  Returns a world transform to integrate a nearby object in an AR experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/setarsession(_:))*