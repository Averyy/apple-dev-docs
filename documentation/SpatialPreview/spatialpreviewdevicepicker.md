# SpatialPreviewDevicePicker

**Framework**: Spatial Preview  
**Kind**: struct  
**Role**: Structure

Presents nearby companion devices and allows the user to make a selection.

**Availability**:
- macOS 27.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency struct SpatialPreviewDevicePicker
```

## Topics

### Initializers
- [init(isPresented: Binding<Bool>, onSelect: (SpatialPreviewEndpoint) -> Void)](./spatialpreviewdevicepicker/init%28ispresented,onselect%29.md)
  Creates a device picker.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Nearby devices
- [struct SpatialPreviewEndpoint](./spatialpreviewendpoint.md)
  An endpoint representing a visionOS device you can connect to for spatial preview.
- [class ConnectedSpatialEndpointObserver](./connectedspatialendpointobserver.md)
  An observer that provides access to the endpoint for a device connected via Mac Virtual Display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/spatialpreviewdevicepicker)*