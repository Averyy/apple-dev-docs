# ARCamera.TrackingState

**Framework**: ARKit  
**Kind**: enum

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
- [ARCamera.TrackingState.notAvailable](arcamera/trackingstate-swift.enum/notavailable.md)
  Camera position tracking is not available.
- [case limited(ARCamera.TrackingState.Reason)](arcamera/trackingstate-swift.enum/limited(_:).md)
  Tracking is available, but the quality of results is questionable.
- [ARCamera.TrackingState.Reason](arcamera/trackingstate-swift.enum/reason.md)
  Causes of limited position-tracking quality.
- [ARCamera.TrackingState.normal](arcamera/trackingstate-swift.enum/normal.md)
  Camera position tracking is providing optimal results.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var trackingState: ARCamera.TrackingState](arcamera/trackingstate-6i3pt.md)
  The general quality of position tracking available when the camera captured a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/trackingstate-swift.enum)*