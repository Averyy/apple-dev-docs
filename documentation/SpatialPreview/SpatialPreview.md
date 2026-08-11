# Spatial Preview

**Framework**: Spatial Preview  
**Kind**: module

Preview spatial content from a macOS app on a connected visionOS device.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

#### Overview

Use Spatial Preview to work with spatial content from a macOS app to a connected visionOS device in real time. The framework centers on two abstractions: [`SpatialPreviewEndpoint`](spatialpreviewendpoint.md), which identifies the target visionOS device, and [`SpatialPreviewSession`](spatialpreviewsession.md), which manages the active preview connection and the flow of content. The [`USDPreviewSession`](usdpreviewsession.md) and [`DocumentPreviewSession`](documentpreviewsession.md) objects adopt `SpatialPreviewSession` and support visionOS previews of Universal Scene Description (USD) content and general file content, respectively. [`USDKit`](https://developer.apple.com/documentation/USDKit) is recommended for Spatial Preview because it works without any additional setup. If you want to use your own OpenUSD library, see the documentation below on how to bridge OpenUSD to [`USDKit`](https://developer.apple.com/documentation/USDKit).

## Topics

### Essentials
- [Working with content from your Mac app using Spatial Preview](working-with-content-from-your-mac-app-using-spatial-preview.md)
  Send and update documents, and work with 3D content live from your macOS app to a visionOS device through the Spatial Preview framework.
- [Bridging an external USD runtime to Spatial Preview](bridging-an-external-usd-runtime-to-spatial-preview.md)
  Sync edits between an app with its own OpenUSD runtime and a Spatial Preview session using a shared layer as the exchange mechanism.
### Nearby devices
- [struct SpatialPreviewEndpoint](spatialpreviewendpoint.md)
  An endpoint representing a visionOS device you can connect to for spatial preview.
- [struct SpatialPreviewDevicePicker](spatialpreviewdevicepicker.md)
  Presents nearby companion devices and allows the user to make a selection.
- [class ConnectedSpatialEndpointObserver](connectedspatialendpointobserver.md)
  An observer that provides access to the endpoint for a device connected via Mac Virtual Display.
### Preview sessions
- [protocol SpatialPreviewSession](spatialpreviewsession.md)
  A session that manages the lifecycle and connection state of a spatial preview on a visionOS device.
- [class DocumentPreviewSession](documentpreviewsession.md)
  A session that streams document content to a connected visionOS device for spatial preview.
- [class USDPreviewSession](usdpreviewsession.md)
  A session that enables you to present the contents of a Universal Scene Description (USD) stage.
### Session state and errors
- [enum SpatialPreviewSessionState](spatialpreviewsessionstate.md)
  Indicates the state of the session and the health of the underlying connection.
- [enum SpatialPreviewSessionError](spatialpreviewsessionerror.md)
- [ConnectedSpatialEndpointObserver.UnavailableError](connectedspatialendpointobserver/unavailableerror.md)
  An error thrown when accessing the [`endpoint`](connectedspatialendpointobserver/endpoint.md) property while no Mac Virtual Display device is available.
- [USDPreviewSession.Error](usdpreviewsession/error.md)
  Errors that can occur during a USD preview session
- [USDPreviewSession.Event](usdpreviewsession/event.md)
  Events emitted during a USD preview session


---

*[View on Apple Developer](https://developer.apple.com/documentation/SpatialPreview)*