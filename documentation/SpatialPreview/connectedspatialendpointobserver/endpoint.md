# endpoint

**Framework**: Spatial Preview  
**Kind**: property

The endpoint for the connected device (if available). If no connected device is available, then an `UnavailableError` error will be thrown. You may choose to discover another device using `SpatialPreviewDevicePicker`.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
final var endpoint: SpatialPreviewEndpoint { get async throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/connectedspatialendpointobserver/endpoint)*