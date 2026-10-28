# getGeoLocation(forPoint:completionHandler:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Converts a position in the framework’s local coordinate system to latitude, longitude and altitude.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
func getGeoLocation(forPoint position: simd_float3, completionHandler: @escaping @Sendable (CLLocationCoordinate2D, CLLocationDistance, (any Error)?) -> Void)
```

```swift
func geoLocation(forPoint position: simd_float3) async throws -> (CLLocationCoordinate2D, CLLocationDistance)
```

```objc
- (void) getGeoLocationForPoint:(simd_float3) position completionHandler:(void (^)(CLLocationCoordinate2D coordinate, CLLocationDistance altitude, NSError *error)) completionHandler;
```

## Discussion

ARKit refers to its local coordinate space as “world” coordinate space, but this is different from geographic coordinates. For more information on ARKit’s coordinate space, see [`setWorldOrigin(relativeTransform:)`](./setworldorigin%28relativetransform%29.md).

To succeed, this function requires an [`ARGeoTrackingConfiguration`](../argeotrackingconfiguration.md) session with state equal to [`ARGeoTrackingStatus.State.localized`](../argeotrackingstatus/state-swift.enum/localized.md).

## Parameters

- `position`: Position in local coordinates to convert.
- `completionHandler`: Code that control will execute when this function returns. The session runs this code on its delegate queue. The parameters are:

  - **coordinate**: Location coordinates (latitude, longitude).
  - **altitude**: The altitude.
  - **error**: The reason, if conversion fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/getgeolocation(forpoint:completionhandler:))*