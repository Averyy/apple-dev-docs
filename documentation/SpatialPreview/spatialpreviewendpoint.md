# SpatialPreviewEndpoint

**Framework**: Spatial Preview  
**Kind**: struct  
**Role**: Structure

An endpoint representing a visionOS device you can connect to for spatial preview.

**Availability**:
- macOS 27.0+
- visionOS

## Declaration

```swift
struct SpatialPreviewEndpoint
```

## Overview

Obtain an endpoint from [`endpoint`](./connectedspatialendpointobserver/endpoint.md) when a device is connected via Mac Virtual Display, or let the user select one with [`SpatialPreviewDevicePicker`](./spatialpreviewdevicepicker.md). Pass the endpoint to [`start(endpoint:)`](./documentpreviewsession/start%28endpoint%29.md) or [`start(endpoint:parameters:viewerOptions:)`](./usdpreviewsession/start%28endpoint,parameters,vieweroptions%29.md) to begin a session.

## Relationships

### Conforms To
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Nearby devices
- [struct SpatialPreviewDevicePicker](./spatialpreviewdevicepicker.md)
  Presents nearby companion devices and allows the user to make a selection.
- [class ConnectedSpatialEndpointObserver](./connectedspatialendpointobserver.md)
  An observer that provides access to the endpoint for a device connected via Mac Virtual Display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/spatialpreviewendpoint)*