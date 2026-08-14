# SpatialPreviewDevicePicker

**Framework**: Spatial Preview  
**Kind**: struct

Presents nearby companion devices and allows the user to make a selection.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct SpatialPreviewDevicePicker
```

## Topics

### Initializers
- [init(isPresented: Binding<Bool>, onSelect: (SpatialPreviewEndpoint) -> Void)](spatialpreviewdevicepicker/init(ispresented:onselect:).md)
  Creates a device picker.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [View](../swiftui/view.md)

## See Also

- [struct SpatialPreviewEndpoint](spatialpreviewendpoint.md)
  An endpoint representing a visionOS device you can connect to for spatial preview.
- [class ConnectedSpatialEndpointObserver](connectedspatialendpointobserver.md)
  An observer that provides access to the endpoint for a device connected via Mac Virtual Display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/spatialpreviewdevicepicker)*