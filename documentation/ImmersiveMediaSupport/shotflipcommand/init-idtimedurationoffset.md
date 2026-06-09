# init(id:time:duration:offset:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a command instance for a certain time, duration and offset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(id: Int, time: CMTime, duration: CMTime, offset: CMTime? = nil)
```

## Parameters

- `id`: The unique ID of this command.
- `time`: The time for this command to start during playback.
- `duration`: The duration of this command during playback.
- `offset`: The offset from the start time of this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/shotflipcommand/init(id:time:duration:offset:))*