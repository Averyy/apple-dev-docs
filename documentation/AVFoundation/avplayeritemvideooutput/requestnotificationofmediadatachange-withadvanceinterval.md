# requestNotificationOfMediaDataChange(withAdvanceInterval:)

**Framework**: AVFoundation  
**Kind**: method

Tells the receiver that the video out put client is entering a quiescent state.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func requestNotificationOfMediaDataChange(withAdvanceInterval interval: TimeInterval)
```

#### Discussion

Call this method before you suspend your use of a [`CVDisplayLink`](https://developer.apple.com/documentation/CoreVideo/CVDisplayLink) type or a [`CADisplayLink`](https://developer.apple.com/documentation/QuartzCore/CADisplayLink) object. After the interval expires, the video output object notifies its delegate that it should resume the display link. If the interval value you specify is large, the delegate is notified as soon as possible rather than waiting.

Do not call this method repeatedly to force the delegate to be notified for each sample.

## Parameters

- `interval`: The amount of time to wait before notifying the delegate of the media change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/requestnotificationofmediadatachange(withadvanceinterval:))*