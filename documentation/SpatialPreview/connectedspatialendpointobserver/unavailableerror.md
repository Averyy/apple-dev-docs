# ConnectedSpatialEndpointObserver.UnavailableError

**Framework**: Spatial Preview  
**Kind**: struct  
**Role**: Structure

An error thrown when accessing the [`endpoint`](./endpoint.md) property while no Mac Virtual Display device is available.

**Availability**:
- macOS 27.0+
- visionOS

## Declaration

```swift
struct UnavailableError
```

## Relationships

### Conforms To
- [Error](../../Swift/error.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Session state and errors
- [enum SpatialPreviewSessionState](../spatialpreviewsessionstate.md)
  Indicates the state of the session and the health of the underlying connection.
- [enum SpatialPreviewSessionError](../spatialpreviewsessionerror.md)
- [USDPreviewSession.Error](../usdpreviewsession/error.md)
  Errors that can occur during a USD preview session
- [USDPreviewSession.Event](../usdpreviewsession/event.md)
  Events emitted during a USD preview session


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/connectedspatialendpointobserver/unavailableerror)*