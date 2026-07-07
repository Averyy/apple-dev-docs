# endpoint

**Framework**: Spatial Preview  
**Kind**: property

The endpoint for the visionOS device currently connected via Mac Virtual Display.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
final var endpoint: SpatialPreviewEndpoint { get async throws }
```

#### Discussion

Check [`isEndpointAvailable`](connectedspatialendpointobserver/isendpointavailable.md) before accessing this property to avoid catching an [`ConnectedSpatialEndpointObserver.UnavailableError`](connectedspatialendpointobserver/unavailableerror.md).

> **Note**: [`ConnectedSpatialEndpointObserver.UnavailableError`](connectedspatialendpointobserver/unavailableerror.md) if no device is currently connected via Mac Virtual Display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/connectedspatialendpointobserver/endpoint)*