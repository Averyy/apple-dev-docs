# direction

**Framework**: Immersive Media Support  
**Kind**: property  
**Role**: Instance Property

Fade direction for this command instance.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var direction: FadeEnvironmentCommand.FadeDirection
```

## See Also

### Instance Properties
- [var duration: CMTime](./duration.md)
  The duration of the command - this can be .zero if the command has no duration
- [var id: Int](./id.md)
  A unique command ID for the immersive media file.
- [var offset: CMTime?](./offset.md)
  The offset from the start time of this command.
- [var opacity: Float](./opacity.md)
  The fade opacity value between `0.0` to `1.0`. This value represents the target opacity of the environment backdrops during playback after fading completes.
- [var time: CMTime](./time.md)
  The time this command starts during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadeenvironmentcommand/direction)*