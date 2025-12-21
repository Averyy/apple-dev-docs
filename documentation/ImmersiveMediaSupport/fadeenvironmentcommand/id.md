# id

**Framework**: Immersive Media Support  
**Kind**: property

A unique command ID for the immersive media file.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var id: Int { get }
```

## See Also

- [var direction: FadeEnvironmentCommand.FadeDirection](fadeenvironmentcommand/direction.md)
  Fade direction for this command instance.
- [var duration: CMTime](fadeenvironmentcommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration
- [var offset: CMTime?](fadeenvironmentcommand/offset.md)
  The offset from the start time of this command.
- [var opacity: Float](fadeenvironmentcommand/opacity.md)
  The fade opacity value between `0.0` to `1.0`. This value represents the target opacity of the environment backdrops during playback after fading completes.
- [var time: CMTime](fadeenvironmentcommand/time.md)
  The time this command starts during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadeenvironmentcommand/id)*