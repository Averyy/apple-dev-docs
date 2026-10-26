# setARSession(_:)

**Framework**: Nearby Interaction  
**Kind**: method  
**Role**: Instance Method

Provides the framework with an existing AR session to use for Camera Assistance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func setARSession(_ session: ARSession)
```

```objc
- (void) setARSession:(ARSession *) session;
```

#### Discussion

Set the [`isCameraAssistanceEnabled`](../ninearbypeerconfiguration/iscameraassistanceenabled.md) flag to `true` before calling this function. If you enable the flag and run a nearby-interaction session without calling [`setARSession(_:)`](./setarsession%28_%29.md), the framework creates an internal [`ARSession`](../../ARKit/arsession.md) instance to which the app has no access.

## Parameters

- `session`: An existing AR session configured as follows:

  - A world-tracking configuration ([`ARWorldTrackingConfiguration`](../../ARKit/arworldtrackingconfiguration.md)) with [`worldAlignment`](../../ARKit/arconfiguration/worldalignment-swift.property.md) `=` [`ARConfiguration.WorldAlignment.gravity`](../../ARKit/arconfiguration/worldalignment-swift.enum/gravity.md), [`isCollaborationEnabled`](../../ARKit/arworldtrackingconfiguration/iscollaborationenabled.md) `=` `false`, [`userFaceTrackingEnabled`](../../ARKit/arworldtrackingconfiguration/userfacetrackingenabled.md) `=` `false`, and [`initialWorldMap`](../../ARKit/arworldtrackingconfiguration/initialworldmap.md) `=` `nil`.
  - A delegate that returns `false` for [`sessionShouldAttemptRelocalization(_:)`](../../ARKit/arsessionobserver/sessionshouldattemptrelocalization%28_%29.md).

## See Also

### Utilizing Camera Assistance
- [func worldTransform(for: NINearbyObject) -> simd_float4x4?](./worldtransform%28for%29.md)
  Returns a world transform to integrate a nearby object in an AR experience.
- [- worldTransformForObject:](./worldtransformforobject_.md)
  Returns a world transform to integrate a nearby object in an AR experience.
- [NINearbyObjectWorldTransformNotAvailable](../ninearbyobjectworldtransformnotavailable.md)
  A constant that indicates that the framework is unable to provide a world transform for a nearby object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/setarsession(_:))*