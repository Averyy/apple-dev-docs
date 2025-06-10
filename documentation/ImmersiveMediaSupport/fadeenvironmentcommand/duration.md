# duration

**Framework**: Immersive Media Support  
**Kind**: property

The duration of the command - this can be .zero if the command has no duration

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var duration: CMTime
```

## See Also

- [var direction: FadeEnvironmentCommand.FadeDirection](fadeenvironmentcommand/direction.md)
  Fade direction for this command instance.
- [var fadeType: FadeEnvironmentCommand.FadeType](fadeenvironmentcommand/fadetype-swift.property.md)
  Fade type for this command instance.
- [var id: Int](fadeenvironmentcommand/id.md)
  An unique command id. Ids should be unique for the whole Immersive Media file.
- [var offset: CMTime?](fadeenvironmentcommand/offset.md)
  Some commands control animations by repeating the command for the whole duration, and specifying the offset of the animation from the start time of this presentation command.
- [var opacity: Float](fadeenvironmentcommand/opacity.md)
  Holds the fade opacity value between 0.0 to 1.0, if the fade type is ‘opacity’. This value represents the target opacity of the environment backdrops during playback after fading completes.
- [var time: CMTime](fadeenvironmentcommand/time.md)
  The time this command starts during playback.
- [var type: PresentationCommandType](fadeenvironmentcommand/type.md)
  The command type (.fadeEnvironment).


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadeenvironmentcommand/duration)*