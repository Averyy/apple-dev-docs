# trackingState

**Framework**: ARKit  
**Kind**: property

The general quality of position tracking available when the camera captured a frame.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var trackingState: ARCamera.TrackingState { get }
```

#### Discussion

When this value is [`ARCamera.TrackingState.limited(_:)`](arcamera/trackingstate-swift.enum/limited(_:).md), see the associated [`ARCamera.TrackingState.Reason`](arcamera/trackingstate-swift.enum/reason.md) value for a possible cause of low tracking quality.

## See Also

- [ARCamera.TrackingState](arcamera/trackingstate-swift.enum.md)
  Values for position tracking quality, with possible causes when tracking quality is limited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/trackingstate-6i3pt)*