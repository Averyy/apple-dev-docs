# startMonitoring()

**Framework**: AVFoundation  
**Kind**: method

Begins monitoring the device’s active scene and making framing recommendations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func startMonitoring() throws
```

## Mentions

- [Adopting smart framing in your camera app](adopting-smart-framing-in-your-camera-app.md)

#### Discussion

The monitor’s [`recommendedFraming`](avcapturesmartframingmonitor/recommendedframing.md) is `nil` when it is not actively running. Call this method to start monitoring. You may start monitoring before or after calling [`startRunning()`](avcapturesession/startrunning().md),  and you may stop active monitoring without stopping the capture session by calling [`stopMonitoring()`](avcapturesmartframingmonitor/stopmonitoring().md) at any time, but you must set [`enabledFramings`](avcapturesmartframingmonitor/enabledframings.md) before running your capture session so that the monitor is prepared for your desired framing recommendations. While the monitor is running, you may set [`enabledFramings`](avcapturesmartframingmonitor/enabledframings.md) at any time to change the framing choices the monitor should consider in its recommendations.

## See Also

- [var isMonitoring: Bool](avcapturesmartframingmonitor/ismonitoring.md)
  Yes when the receiver is actively monitoring.
- [func stopMonitoring()](avcapturesmartframingmonitor/stopmonitoring.md)
  Stops monitoring the device’s active scene and making framing recommendations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor/startmonitoring())*