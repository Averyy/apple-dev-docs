# init(id:time:duration:direction:color:offset:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes a color fade command.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(id: Int, time: CMTime, duration: CMTime, direction: FadeCommand.FadeDirection, color: simd_float3, offset: CMTime? = nil)
```

## Parameters

- `id`: The unique ID of this command.
- `time`: The time this command starts during playback.
- `duration`: The duration of the command. This can be   if the command has no duration.
- `direction`: The fade direction for this command instance.
- `color`: The fade color.
- `offset`: The offset from the start time of this command. This parameter is usually unused and let in control of a  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadecommand/init(id:time:duration:direction:color:offset:))*