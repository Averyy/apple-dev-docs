# USDPreviewSession.Event

**Framework**: Spatial Preview  
**Kind**: enum

Events emitted during a USD preview session

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
enum Event
```

## Topics

### Enumeration Cases
- [case error(USDPreviewSession.Error)](usdpreviewsession/event/error(_:).md)
  Session error (editing read-only stage, etc.)
- [USDPreviewSession.Event.playbackStateChanged(isPlaying:)](usdpreviewsession/event/playbackstatechanged(isplaying:).md)
  The USD’s animation playback state has changed
- [USDPreviewSession.Event.timeChanged(_:)](usdpreviewsession/event/timechanged(_:).md)
  The USD animation timecode has changed

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum SpatialPreviewSessionState](spatialpreviewsessionstate.md)
  Indicates the state of the session and the health of the underlying connection.
- [enum SpatialPreviewSessionError](spatialpreviewsessionerror.md)
- [ConnectedSpatialEndpointObserver.UnavailableError](connectedspatialendpointobserver/unavailableerror.md)
  An error thrown when accessing the [`endpoint`](connectedspatialendpointobserver/endpoint.md) property while no Mac Virtual Display device is available.
- [USDPreviewSession.Error](usdpreviewsession/error.md)
  Errors that can occur during a USD preview session


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/event)*