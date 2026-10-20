# ARCamera.TrackingState.Reason.excessiveMotion

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

The device is moving too fast for accurate image-based position tracking.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
case excessiveMotion
```

## See Also

### Inhibitors of Tracking Quality
- [ARCamera.TrackingState.Reason.initializing](./initializing.md)
  The AR session has not gathered enough camera or motion data to provide tracking information.
- [ARCamera.TrackingState.Reason.relocalizing](./relocalizing.md)
  The AR session is attempting to resume after an interruption.
- [ARCamera.TrackingState.Reason.insufficientFeatures](./insufficientfeatures.md)
  The scene visible to the camera doesn’t contain enough distinguishable features for image-based position tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/trackingstate-swift.enum/reason/excessivemotion)*