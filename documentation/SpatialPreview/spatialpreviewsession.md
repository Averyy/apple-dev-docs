# SpatialPreviewSession

**Framework**: Spatial Preview  
**Kind**: protocol

A session that manages the lifecycle and connection state of a spatial preview on a visionOS device.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
protocol SpatialPreviewSession : AnyObject, Observable
```

## Topics

### Instance Properties
- [var progress: ProgressReporter](spatialpreviewsession/progress.md)
  Reports the progress of the session
- [var state: SpatialPreviewSessionState](spatialpreviewsession/state.md)
  Can observe this state
### Instance Methods
- [func close() async throws](spatialpreviewsession/close.md)
  Gracefully close the session

## Relationships

### Inherits From
- [Observable](../Observation/Observable.md)
### Conforming Types
- [DocumentPreviewSession](documentpreviewsession.md)
- [USDPreviewSession](usdpreviewsession.md)

## See Also

- [class DocumentPreviewSession](documentpreviewsession.md)
  Document session allows you to present the contents of a URL or Data.
- [class USDPreviewSession](usdpreviewsession.md)
  A session that enables you to present the contents of a Universal Scene Description (USD) stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/spatialpreviewsession)*