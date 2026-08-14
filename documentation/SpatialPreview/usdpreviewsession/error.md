# USDPreviewSession.Error

**Framework**: Spatial Preview  
**Kind**: enum

Errors that can occur during a USD preview session

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
enum Error
```

## Topics

### Enumeration Cases
- [USDPreviewSession.Error.assetUnshareable](usdpreviewsession/error/assetunshareable.md)
  The stage became too complex to sync.
- [USDPreviewSession.Error.readOnlyStage](usdpreviewsession/error/readonlystage.md)
  The stage was replaced during optimization and any changes made to the stage won’t be synced.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum SpatialPreviewSessionState](spatialpreviewsessionstate.md)
  Indicates the state of the session and the health of the underlying connection.
- [enum SpatialPreviewSessionError](spatialpreviewsessionerror.md)
- [ConnectedSpatialEndpointObserver.UnavailableError](connectedspatialendpointobserver/unavailableerror.md)
  An error thrown when accessing the [`endpoint`](connectedspatialendpointobserver/endpoint.md) property while no Mac Virtual Display device is available.
- [USDPreviewSession.Event](usdpreviewsession/event.md)
  Events emitted during a USD preview session


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/error)*