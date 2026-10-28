# endpoint

**Framework**: Spatial Preview  
**Kind**: property  
**Role**: Instance Property

The endpoint for the visionOS device currently connected via Mac Virtual Display.

**Availability**:
- macOS 27.0+
- visionOS

## Declaration

```swift
@MainActor
final var endpoint: SpatialPreviewEndpoint { get async throws }
```

## Discussion

Check [`isEndpointAvailable`](./isendpointavailable.md) before accessing this property to avoid catching an [`ConnectedSpatialEndpointObserver.UnavailableError`](./unavailableerror.md).

> **Throws**: [`ConnectedSpatialEndpointObserver.UnavailableError`](./unavailableerror.md) if no device is currently connected via Mac Virtual Display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/connectedspatialendpointobserver/endpoint)*