# init(time:duration:direction:opacity:offset:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes an opacity fade command.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(time: CMTime, duration: CMTime, direction: FadeEnvironmentCommand.FadeDirection, opacity: Float, offset: CMTime? = nil)
```

## Parameters

- `time`: The time this command starts during playback.
- `duration`: The duration of the command - this can be .zero if the command has no duration.
- `direction`: Fade direction for this command instance.
- `opacity`: Fade opacity.
- `offset`: The offset from the start time of this command. This parameter is usually unused and let in control of a PresentationDescriptorReader.

## See Also

- [init(from: any Decoder) throws](fadeenvironmentcommand/init(from:).md)
  Creates a FadeEnvironmentCommand from the specified decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadeenvironmentcommand/init(time:duration:direction:opacity:offset:))*