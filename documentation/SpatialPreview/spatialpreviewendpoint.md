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
- [CustomReflectable](../swift/customreflectable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct SpatialPreviewDevicePicker](spatialpreviewdevicepicker.md)
  Presents nearby companion devices and allows the user to make a selection.
- [class ConnectedSpatialEndpointObserver](connectedspatialendpointobserver.md)
  An observer that provides access to the endpoint for a device connected via Mac Virtual Display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/spatialpreviewendpoint)*