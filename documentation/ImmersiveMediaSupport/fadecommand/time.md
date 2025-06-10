# time

**Framework**: Immersive Media Support  
**Kind**: property

The time this command starts during playback.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var time: CMTime
```

## See Also

- [var color: simd_float3?](fadecommand/color.md)
  Represents the fade color value between 0.0 to 1.0 for each color channel, if the fade type is ‘color’. If color set to ‘black’, and the direction is ‘in’, then it fades from black color to the video frame.
- [var direction: FadeCommand.FadeDirection](fadecommand/direction.md)
  Fade direction for this command instance.
- [var duration: CMTime](fadecommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration
- [var fadeType: FadeCommand.FadeType](fadecommand/fadetype-swift.property.md)
  Fade type for this command instance.
- [var id: Int](fadecommand/id.md)
  An unique command id. Ids should be unique for the whole Immersive Media file.
- [var offset: CMTime?](fadecommand/offset.md)
  Some commands control animations by repeating the command for the whole duration, and specifying the offset of the animation from the start time of this presentation command.
- [var type: PresentationCommandType](fadecommand/type.md)
  The command type (.fade).


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadecommand/time)*