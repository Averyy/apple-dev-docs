# stopMonitoring()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Stops monitoring the device’s active scene and making framing recommendations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func stopMonitoring()
```

```objc
- (void) stopMonitoring;
```

## Mentions

- [Adopting smart framing in your camera app](../adopting-smart-framing-in-your-camera-app.md)

#### Discussion

The monitor’s [`recommendedFraming`](./recommendedframing.md) is `nil` when it is not actively running. Call this method to stop actively monitoring the scene and making framing recommendations. You may start monitoring before or after calling [`startRunning()`](../avcapturesession/startrunning%28%29.md), and may stop active monitoring without stopping the capture session by calling [`stopMonitoring()`](./stopmonitoring%28%29.md) at any time.

## See Also

### Managing the life cycle
- [var isMonitoring: Bool](./ismonitoring.md)
  Yes when the receiver is actively monitoring.
- [func startMonitoring() throws](./startmonitoring%28%29.md)
  Begins monitoring the device’s active scene and making framing recommendations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor/stopmonitoring())*