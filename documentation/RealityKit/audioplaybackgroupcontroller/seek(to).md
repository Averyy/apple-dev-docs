# seek(to:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Sets the playback position to the specified time.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency func seek(to time: Duration)
```

## Parameters

- `time`: The desired playback position.

## See Also

### Controlling playback
- [func play(at: AVAudioTime) throws](./play%28at%29.md)
  Plays all audio resources in the group asynchronously at a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller/seek(to:))*