# DocumentPreviewSession

**Framework**: Spatial Preview  
**Kind**: class

A session that streams document content to a connected visionOS device for spatial preview.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
final class DocumentPreviewSession
```

## Mentions

- [Bridging an application’s custom USD runtime to Spatial Preview](bridging-an-external-usd-runtime-to-spatial-preview.md)

#### Overview

To start a `DocumentPreviewSession` preview, obtain an [`SpatialPreviewEndpoint`](spatialpreviewendpoint.md) through one of two paths:

- Use [`ConnectedSpatialEndpointObserver`](connectedspatialendpointobserver.md) when the visionOS device is already connected using Mac Virtual Display. Observe its [`isEndpointAvailable`](connectedspatialendpointobserver/isendpointavailable.md) property to know when a device is ready, then access its [`endpoint`](connectedspatialendpointobserver/endpoint.md) property to retrieve the endpoint.
- Use [`SpatialPreviewDevicePicker`](spatialpreviewdevicepicker.md), a [`View`](https://developer.apple.com/documentation/SwiftUI/View) that presents nearby companion devices and calls its closure with the chosen `SpatialPreviewEndpoint`, when you want to let someone select a device interactively.

When you have the endpoint, create a `DocumentPreviewSession`, the concrete session class that conforms to [`SpatialPreviewSession`](spatialpreviewsession.md) and [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable). Initialize the session with a display name and the [`UTType`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTType-swift.struct) of the content, then call [`start(endpoint:)`](documentpreviewsession/start(endpoint:).md) with the endpoint to open the connection:

```swift
let observer = ConnectedSpatialEndpointObserver()

// Wait for a device to become available.
let endpoint = try await observer.endpoint

// Create and start the session.
let session = DocumentPreviewSession(name: "My Spatial Content", contentType: .jpeg)

try await session.start(endpoint: endpoint)

// Push initial content, then update as the document changes.
let spatialContentURL = URL(filePath: "/path/to/spatialContent.jpeg")
try await session.updateContents(url: spatialContentURL)
```

After starting a session, use [`updateContents(data:)`](documentpreviewsession/updatecontents(data:).md) to push a [`Data`](https://developer.apple.com/documentation/Foundation/Data) value directly to the device; this is useful when your document content is already in memory. Use [`updateContents(url:)`](documentpreviewsession/updatecontents(url:).md) to stream content from a file URL, which avoids loading the entire file into memory at once. Call either method each time the document changes.

Track connection changes using [`SpatialPreviewSessionState`](spatialpreviewsessionstate.md). When you finish, call [`close()`](spatialpreviewsession/close().md) to end the session cleanly.

## Topics

### Initializers
- [convenience init(name: String, contentType: UTType)](documentpreviewsession/init(name:contenttype:).md)
  Create a new DocumentPreviewSession with the name and contentType, to be used for all content updates.
### Instance Properties
- [let contentType: UTType](documentpreviewsession/contenttype.md)
  The content type of the document. All updates must provide documents conforming to this content type.
- [let name: String](documentpreviewsession/name.md)
  The display name of the document on the spatial preview
### Instance Methods
- [func start(endpoint: SpatialPreviewEndpoint) async throws](documentpreviewsession/start(endpoint:).md)
  Connects to the specified endpoint and prepares the session to send document updates.
- [func updateContents(data: Data) async throws](documentpreviewsession/updatecontents(data:).md)
  Update the contents of the document with the provided data.
- [func updateContents(url: URL) async throws](documentpreviewsession/updatecontents(url:).md)
  Update the contents of the document with the provided URL.

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
- [class USDPreviewSession](usdpreviewsession.md)
  A session that enables you to present the contents of a Universal Scene Description (USD) stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/documentpreviewsession)*