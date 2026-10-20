# start(endpoint:parameters:viewerOptions:)

**Framework**: Spatial Preview  
**Kind**: method  
**Role**: Instance Method

Connects to the specified endpoint and begins streaming the USD stage for spatial preview.

**Availability**:
- macOS 27.0+
- visionOS

## Declaration

```swift
nonisolated
(nonsending) final func start(endpoint: SpatialPreviewEndpoint, parameters: USDPreviewSession.OptimizationParameters = .processed([.optimized, .compressed]), viewerOptions: USDPreviewSession.SpatialViewerOptions = .default) async throws
```

#### Discussion

The session automatically optimizes and compresses the `USDStage` to ensure it runs well on visionOS. Pass [`USDPreviewSession.OptimizationParameters.unmodified`](./optimizationparameters/unmodified.md) to opt out of this feature. Disabling optimization may cause the session to throw [`USDPreviewSession.Error.assetUnshareable`](./error/assetunshareable.md).

> **Throws**: [`USDPreviewSession.Error.assetUnshareable`](./error/assetunshareable.md) if the stage complexity exceeds the capabilities of the session; or a [`SpatialPreviewSessionError`](../spatialpreviewsessionerror.md) if the connection cannot be established.

## Parameters

- `endpoint`: The destination endpoint representing the device to connect to.
- `parameters`: The optimization strategy to apply to the stage before transmission. Defaults to [`USDPreviewSession.OptimizationParameters.processed(_:)`](./optimizationparameters/processed%28_%29.md) with both `.optimized` and `.compressed` steps enabled.
- `viewerOptions`: Interaction capabilities to enable in the remote viewer, such as export, annotations, and per-object manipulation. Defaults to [`default`](./spatialvieweroptions/default.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/start(endpoint:parameters:vieweroptions:))*