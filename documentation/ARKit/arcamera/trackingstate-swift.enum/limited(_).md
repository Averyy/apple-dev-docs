# ARCamera.TrackingState.limited(_:)

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

Tracking is available, but the quality of results is questionable.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
case limited(ARCamera.TrackingState.Reason)
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](../../managing-session-life-cycle-and-tracking-quality.md)

## Discussion

In this state, the positions and transforms of anchors in the scene (especially detected planes) may not be accurate or consistent from one captured frame to the next.

See the associated [`ARCamera.TrackingState.Reason`](./reason.md) value for information you can present to the user for improving tracking quality.

## See Also

### Determining the camera tracking status
- [ARCamera.TrackingState.notAvailable](./notavailable.md)
  Camera position tracking is not available.
- [ARCamera.TrackingState.Reason](./reason.md)
  Causes of limited position-tracking quality.
- [ARCamera.TrackingState.normal](./normal.md)
  Camera position tracking is providing optimal results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/trackingstate-swift.enum/limited(_:))*