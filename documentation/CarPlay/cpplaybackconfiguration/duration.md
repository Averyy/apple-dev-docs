# duration

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The duration of the media file in seconds.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var duration: CMTime { get }
```

```objc
@property (nonatomic, assign, readonly) CMTime duration;
```

## Discussion

The system uses this value and the value in the [`elapsedTime`](./elapsedtime.md) property to determine the playback progress. If the duration of the media file is unknown or unavailable, the value of this property is `0`. For example, the value is typically `0` for live-streaming content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration/duration)*