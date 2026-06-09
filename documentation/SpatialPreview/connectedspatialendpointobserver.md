# ConnectedSpatialEndpointObserver

**Framework**: Spatial Preview  
**Kind**: class

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
final class ConnectedSpatialEndpointObserver
```

## Topics

### Structures
- [ConnectedSpatialEndpointObserver.UnavailableError](connectedspatialendpointobserver/unavailableerror.md)
  An error thrown when accessing the [`endpoint`](connectedspatialendpointobserver/endpoint.md) property while no Mac Virtual Display device is available.
### Initializers
- [init()](connectedspatialendpointobserver/init.md)
  Creates a new observer for monitoring connected device endpoint availability.
### Instance Properties
- [var endpoint: SpatialPreviewEndpoint](connectedspatialendpointobserver/endpoint.md)
  The endpoint for the connected device (if available). If no connected device is available, then an `UnavailableError` error will be thrown. You may choose to discover another device using `SpatialPreviewDevicePicker`.
- [var isEndpointAvailable: Bool](connectedspatialendpointobserver/isendpointavailable.md)
  Indicates whether a connected device endpoint is currently connected.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct SpatialPreviewEndpoint](spatialpreviewendpoint.md)
  An endpoint representing a destination that that can be connected to
- [struct SpatialPreviewDevicePicker](spatialpreviewdevicepicker.md)
  Presents nearby companion devices and allows the user to make a selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/connectedspatialendpointobserver)*