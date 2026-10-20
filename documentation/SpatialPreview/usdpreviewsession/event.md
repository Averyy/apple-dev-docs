# USDPreviewSession.Event

**Framework**: Spatial Preview  
**Kind**: enum  
**Role**: Enumeration

Events emitted during a USD preview session

**Availability**:
- macOS 27.0+
- visionOS

## Declaration

```swift
enum Event
```

## Topics

### Enumeration Cases
- [case error(USDPreviewSession.Error)](./event/error%28_%29.md)
  Session error (editing read-only stage, etc.)
- [USDPreviewSession.Event.playbackStateChanged(isPlaying:)](./event/playbackstatechanged%28isplaying%29.md)
  The USD’s animation playback state has changed
- [USDPreviewSession.Event.timeChanged(_:)](./event/timechanged%28_%29.md)
  The USD animation timecode has changed

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Session state and errors
- [enum SpatialPreviewSessionState](../spatialpreviewsessionstate.md)
  Indicates the state of the session and the health of the underlying connection.
- [enum SpatialPreviewSessionError](../spatialpreviewsessionerror.md)
- [ConnectedSpatialEndpointObserver.UnavailableError](../connectedspatialendpointobserver/unavailableerror.md)
  An error thrown when accessing the [`endpoint`](../connectedspatialendpointobserver/endpoint.md) property while no Mac Virtual Display device is available.
- [USDPreviewSession.Error](./error.md)
  Errors that can occur during a USD preview session


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/event)*