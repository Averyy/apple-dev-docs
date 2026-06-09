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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct SpatialPreviewEndpoint](spatialpreviewendpoint.md)
  An endpoint representing a destination that that can be connected to
- [class ConnectedSpatialEndpointObserver](connectedspatialendpointobserver.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/spatialpreviewdevicepicker)*