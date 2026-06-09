# init(isPresented:onSelect:)

**Framework**: Spatial Preview  
**Kind**: init

Creates a device picker.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency init(isPresented: Binding<Bool>, onSelect: @escaping (SpatialPreviewEndpoint) -> Void)
```

## Parameters

- `isPresented`: A binding to a Boolean that determines whether the picker view is displayed
- `onSelect`: When a device is selected the `SpatialPreviewEndpoint` for that device will be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/spatialpreviewdevicepicker/init(ispresented:onselect:))*