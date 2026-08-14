# ConnectedSpatialEndpointObserver

**Framework**: Spatial Preview  
**Kind**: class

An observer that provides access to the endpoint for a device connected via Mac Virtual Display.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
final class ConnectedSpatialEndpointObserver
```

#### Overview

You can choose to discover another device using [`SpatialPreviewDevicePicker`](spatialpreviewdevicepicker.md).

## Topics

### Structures
- [ConnectedSpatialEndpointObserver.UnavailableError](connectedspatialendpointobserver/unavailableerror.md)
  An error thrown when accessing the [`endpoint`](connectedspatialendpointobserver/endpoint.md) property while no Mac Virtual Display device is available.
### Initializers
- [init()](connectedspatialendpointobserver/init.md)
  Creates a new observer for monitoring connected device endpoint availability.
### Instance Properties
- [var endpoint: SpatialPreviewEndpoint](connectedspatialendpointobserver/endpoint.md)
  The endpoint for the visionOS device currently connected via Mac Virtual Display.
- [var isEndpointAvailable: Bool](connectedspatialendpointobserver/isendpointavailable.md)
  Indicates whether a connected device endpoint is currently connected.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [Observable](../observation/observable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct SpatialPreviewEndpoint](spatialpreviewendpoint.md)
  An endpoint representing a visionOS device you can connect to for spatial preview.
- [struct SpatialPreviewDevicePicker](spatialpreviewdevicepicker.md)
  Presents nearby companion devices and allows the user to make a selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/connectedspatialendpointobserver)*