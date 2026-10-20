# ARCamera.TrackingState

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Values for position tracking quality, with possible causes when tracking quality is limited.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
@frozen
enum TrackingState
```

## Topics

### Determining the camera tracking status
- [ARCamera.TrackingState.notAvailable](./trackingstate-swift.enum/notavailable.md)
  Camera position tracking is not available.
- [case limited(ARCamera.TrackingState.Reason)](./trackingstate-swift.enum/limited%28_%29.md)
  Tracking is available, but the quality of results is questionable.
- [ARCamera.TrackingState.Reason](./trackingstate-swift.enum/reason.md)
  Causes of limited position-tracking quality.
- [ARCamera.TrackingState.normal](./trackingstate-swift.enum/normal.md)
  Camera position tracking is providing optimal results.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling Tracking Status
- [var trackingState: ARCamera.TrackingState](./trackingstate-6i3pt.md)
  The general quality of position tracking available when the camera captured a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/trackingstate-swift.enum)*