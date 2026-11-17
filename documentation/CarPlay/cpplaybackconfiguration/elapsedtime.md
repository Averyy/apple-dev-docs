# elapsedTime

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The elapsed time since the start of playback.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var elapsedTime: CMTime { get }
```

```objc
@property (nonatomic, assign, readonly) CMTime elapsedTime;
```

## Discussion

For a paused item, this value represents the amount of the media file already played. For live-streamed content, this value might represent the amount of time from the beginning of the event or the point at which someone joined the stream. The system uses this value and the value in the [`duration`](./duration.md) property to determine the playback progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration/elapsedtime)*