# SpatialPreviewEndpoint

**Framework**: Spatial Preview  
**Kind**: struct

An endpoint representing a visionOS device you can connect to for spatial preview.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct SpatialPreviewEndpoint
```

#### Overview

Obtain an endpoint from [`endpoint`](connectedspatialendpointobserver/endpoint.md) when a device is connected via Mac Virtual Display, or let the user select one with [`SpatialPreviewDevicePicker`](spatialpreviewdevicepicker.md). Pass the endpoint to [`start(endpoint:)`](documentpreviewsession/start(endpoint:).md) or [`start(endpoint:parameters:viewerOptions:)`](usdpreviewsession/start(endpoint:parameters:vieweroptions:).md) to begin a session.

## Relationships

### Conforms To
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct SpatialPreviewDevicePicker](spatialpreviewdevicepicker.md)
  Presents nearby companion devices and allows the user to make a selection.
- [class ConnectedSpatialEndpointObserver](connectedspatialendpointobserver.md)
  An observer that provides access to the endpoint for a device connected via Mac Virtual Display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/spatialpreviewendpoint)*