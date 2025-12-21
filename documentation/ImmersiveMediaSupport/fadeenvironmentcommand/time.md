# time

**Framework**: Immersive Media Support  
**Kind**: property

The time this command starts during playback.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var time: CMTime
```

## See Also

- [var direction: FadeEnvironmentCommand.FadeDirection](fadeenvironmentcommand/direction.md)
  Fade direction for this command instance.
- [var duration: CMTime](fadeenvironmentcommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration
- [var id: Int](fadeenvironmentcommand/id.md)
  A unique command ID for the immersive media file.
- [var offset: CMTime?](fadeenvironmentcommand/offset.md)
  The offset from the start time of this command.
- [var opacity: Float](fadeenvironmentcommand/opacity.md)
  The fade opacity value between `0.0` to `1.0`. This value represents the target opacity of the environment backdrops during playback after fading completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadeenvironmentcommand/time)*