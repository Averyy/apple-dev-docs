# init(id:time:duration:direction:opacity:offset:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a fade environment command instance.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(id: Int, time: CMTime, duration: CMTime, direction: FadeEnvironmentCommand.FadeDirection, opacity: Float, offset: CMTime? = nil)
```

## Parameters

- `id`: The unique ID of this command.
- `time`: The time this command starts during playback.
- `duration`: The duration of the command. This can be   if the command doesn’t have a specific duration.
- `direction`: The fade direction for this command instance.
- `opacity`: The fade opacity.
- `offset`: The offset from the start time of this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadeenvironmentcommand/init(id:time:duration:direction:opacity:offset:))*