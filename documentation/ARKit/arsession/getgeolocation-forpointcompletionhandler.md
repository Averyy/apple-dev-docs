# getGeoLocation(forPoint:completionHandler:)

**Framework**: ARKit  
**Kind**: method

Converts a position in the framework’s local coordinate system to latitude, longitude and altitude.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func geoLocation(forPoint position: simd_float3) async throws -> (CLLocationCoordinate2D, CLLocationDistance)
```

#### Discussion

ARKit refers to its local coordinate space as “world” coordinate space, but this is different from geographic coordinates. For more information on ARKit’s coordinate space, see [`setWorldOrigin(relativeTransform:)`](arsession/setworldorigin(relativetransform:).md).

To succeed, this function requires an [`ARGeoTrackingConfiguration`](argeotrackingconfiguration.md) session with state equal to [`ARGeoTrackingStatus.State.localized`](argeotrackingstatus/state-swift.enum/localized.md).

## Parameters

- `position`: Position in local coordinates to convert.
- `completionHandler`: Code that control will execute when this function returns. The session runs this code on its delegate queue. The parameters are:


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/getgeolocation(forpoint:completionhandler:))*