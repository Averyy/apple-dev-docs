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

- [Bridging an application’s custom USD runtime to Spatial Preview](bridging-an-external-usd-runtime-to-spatial-preview.md)

#### Overview

To create a `USDPreviewSession`, initialize one with a [`USDStage`](https://developer.apple.com/documentation/USDKit/USDStage-4sfi1) from [`USDKit`](https://developer.apple.com/documentation/USDKit):

```swift
let observer = ConnectedSpatialEndpointObserver()

let session = USDPreviewSession(stage: usdStage)

// Wait for a device to become available.
let endpoint = try await observer.endpoint

try await session.start(endpoint: endpoint)
```

After [`start(endpoint:parameters:viewerOptions:)`](usdpreviewsession/start(endpoint:parameters:vieweroptions:).md) returns, the session’s `state` transitions to [`SpatialPreviewSessionState.connected`](spatialpreviewsessionstate/connected.md) and the device starts loading the USD content. Then use [`USDKit`](https://developer.apple.com/documentation/USDKit) to make edits to the [`USDStage`](https://developer.apple.com/documentation/USDKit/USDStage-4sfi1) to update the content. Changes on visionOS are automatically synchronized back to [`USDKit`](https://developer.apple.com/documentation/USDKit) in your macOS app.

## Topics

### Structures
- [USDPreviewSession.OptimizationSteps](usdpreviewsession/optimizationsteps.md)
  A set of optimization steps to apply to a USD stage before previewing on a device.
- [USDPreviewSession.SpatialViewerOptions](usdpreviewsession/spatialvieweroptions.md)
  Configuration options that control interaction capabilities for a USD document session.
### Initializers
- [convenience init(stage: USDStage)](usdpreviewsession/init(stage:).md)
### Instance Properties
- [let events: any AsyncSequence<USDPreviewSession.Event, Never>](usdpreviewsession/events.md)
  Async sequence of session events
- [var isPlaying: Bool](usdpreviewsession/isplaying.md)
- [var time: TimeInterval](usdpreviewsession/time.md)
### Instance Methods
- [func start(endpoint: SpatialPreviewEndpoint, parameters: USDPreviewSession.OptimizationParameters, viewerOptions: USDPreviewSession.SpatialViewerOptions) async throws](usdpreviewsession/start(endpoint:parameters:vieweroptions:).md)
### Enumerations
- [USDPreviewSession.Error](usdpreviewsession/error.md)
  Errors that can occur during a USD preview session
- [USDPreviewSession.Event](usdpreviewsession/event.md)
  Events emitted during a USD preview session
- [USDPreviewSession.OptimizationParameters](usdpreviewsession/optimizationparameters.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpatialPreviewSession](spatialpreviewsession.md)

## See Also

- [protocol SpatialPreviewSession](spatialpreviewsession.md)
  A session that manages the lifecycle and connection state of a spatial preview on a visionOS device.
- [class DocumentPreviewSession](documentpreviewsession.md)
  Document session allows you to present the contents of a URL or Data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession)*