# init(id:time:duration:direction:opacity:offset:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes an opacity fade command.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(id: Int, time: CMTime, duration: CMTime, direction: FadeEnvironmentCommand.FadeDirection, opacity: Float, offset: CMTime? = nil)
```

## Parameters

- `id`: The unique id of this command.
- `time`: The time this command starts during playback.
- `duration`: The duration of the command - this can be .zero if the command has no duration.
- `direction`: Fade direction for this command instance.
- `opacity`: Fade opacity.
- `offset`: The offset from the start time of this command. This parameter is usually unused and let in control of a  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadeenvironmentcommand/init(id:time:duration:direction:opacity:offset:))*