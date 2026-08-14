# USDPreviewSession

**Framework**: Spatial Preview  
**Kind**: class

A session that enables you to present the contents of a Universal Scene Description (USD) stage.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
final class USDPreviewSession
```

## Mentions

- [Bridging an external USD runtime to Spatial Preview](bridging-an-external-usd-runtime-to-spatial-preview.md)

#### Overview

To create a `USDPreviewSession`, initialize one with a [`USDStage`](https://developer.apple.com/documentation/usdkit/usdstage) from [`USDKit`](https://developer.apple.com/documentation/usdkit):

```swift
let observer = ConnectedSpatialEndpointObserver()

let session = USDPreviewSession(stage: usdStage)

// Wait for a device to become available.
let endpoint = try await observer.endpoint

try await session.start(endpoint: endpoint)
```

After [`start(endpoint:parameters:viewerOptions:)`](usdpreviewsession/start(endpoint:parameters:vieweroptions:).md) returns, the session’s `state` transitions to [`SpatialPreviewSessionState.connected`](spatialpreviewsessionstate/connected.md) and the device starts loading the USD content. Then use [`USDKit`](https://developer.apple.com/documentation/usdkit) to make edits to the [`USDStage`](https://developer.apple.com/documentation/usdkit/usdstage) to update the content. Changes on visionOS are automatically synchronized back to [`USDKit`](https://developer.apple.com/documentation/usdkit) in your macOS app.

## Topics

### Protocols
- [USDPreviewSession.ChangeListDelegate](usdpreviewsession/changelistdelegate.md)
  A protocol to provide shared undo/redo tracking in a USDPreviewSession.
### Structures
- [USDPreviewSession.OptimizationSteps](usdpreviewsession/optimizationsteps.md)
  A set of optimization steps to apply to a USD stage before previewing on a device.
- [USDPreviewSession.SpatialViewerOptions](usdpreviewsession/spatialvieweroptions.md)
  Configuration options that control interaction capabilities for a USD document session.
### Initializers
- [convenience init(stage: USDStage)](usdpreviewsession/init(stage:).md)
### Instance Properties
- [var delegate: (any USDPreviewSession.ChangeListDelegate)?](usdpreviewsession/delegate.md)
  Optional synchronous undo/redo event delegate
- [let events: any AsyncSequence<USDPreviewSession.Event, Never>](usdpreviewsession/events.md)
  Async sequence of session events
- [var isPlaying: Bool](usdpreviewsession/isplaying.md)
- [var time: TimeInterval](usdpreviewsession/time.md)
### Instance Methods
- [func start(endpoint: SpatialPreviewEndpoint, parameters: USDPreviewSession.OptimizationParameters, viewerOptions: USDPreviewSession.SpatialViewerOptions) async throws](usdpreviewsession/start(endpoint:parameters:vieweroptions:).md)
  Connects to the specified endpoint and begins streaming the USD stage for spatial preview.
- [func updateUndoRedoCounts(undo: UInt, redo: UInt) async throws](usdpreviewsession/updateundoredocounts(undo:redo:).md)
  Update the count of undoable and redoable actions in the USDPreviewSession which is reflected in the UI on visionOS.
### Enumerations
- [USDPreviewSession.Error](usdpreviewsession/error.md)
  Errors that can occur during a USD preview session
- [USDPreviewSession.Event](usdpreviewsession/event.md)
  Events emitted during a USD preview session
- [USDPreviewSession.OptimizationParameters](usdpreviewsession/optimizationparameters.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [Observable](../observation/observable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SpatialPreviewSession](spatialpreviewsession.md)

## See Also

- [protocol SpatialPreviewSession](spatialpreviewsession.md)
  A session that manages the lifecycle and connection state of a spatial preview on a visionOS device.
- [class DocumentPreviewSession](documentpreviewsession.md)
  A session that streams document content to a connected visionOS device for spatial preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession)*