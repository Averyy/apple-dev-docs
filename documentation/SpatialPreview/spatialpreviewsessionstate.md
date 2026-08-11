# SpatialPreviewSessionState

**Framework**: Spatial Preview  
**Kind**: enum

Indicates the state of the session and the health of the underlying connection.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
enum SpatialPreviewSessionState
```

## Mentions

- [Bridging an external USD runtime to Spatial Preview](bridging-an-external-usd-runtime-to-spatial-preview.md)

## Topics

### Enumeration Cases
- [SpatialPreviewSessionState.connected](spatialpreviewsessionstate/connected.md)
  The session is actively connected
- [SpatialPreviewSessionState.interrupted](spatialpreviewsessionstate/interrupted.md)
  The session connection has been interrupted, but may resume.
- [SpatialPreviewSessionState.invalidated](spatialpreviewsessionstate/invalidated.md)
  The sesion has been invalidated and is no longer available.
- [SpatialPreviewSessionState.waiting](spatialpreviewsessionstate/waiting.md)
  The session has been created, but not started.
### Instance Properties
- [var isInvalidated: Bool](spatialpreviewsessionstate/isinvalidated.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum SpatialPreviewSessionError](spatialpreviewsessionerror.md)
- [ConnectedSpatialEndpointObserver.UnavailableError](connectedspatialendpointobserver/unavailableerror.md)
  An error thrown when accessing the [`endpoint`](connectedspatialendpointobserver/endpoint.md) property while no Mac Virtual Display device is available.
- [USDPreviewSession.Error](usdpreviewsession/error.md)
  Errors that can occur during a USD preview session
- [USDPreviewSession.Event](usdpreviewsession/event.md)
  Events emitted during a USD preview session


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/spatialpreviewsessionstate)*