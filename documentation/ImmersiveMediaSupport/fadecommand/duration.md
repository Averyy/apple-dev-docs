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

- [var color: simd_float3?](fadecommand/color.md)
  The fade color value between 0.0 to 1.0 for each color channel. If color is set to black, and the direction is `in`, then it fades from black color to the video frame.
- [var direction: FadeCommand.FadeDirection](fadecommand/direction.md)
  Fade direction for this command instance.
- [var id: Int](fadecommand/id.md)
  A unique command id. Ids should be unique for the whole Immersive Media file.
- [var offset: CMTime?](fadecommand/offset.md)
  Some commands control animations by repeating the command for the whole duration, and specifying the offset of the animation from the start time of this presentation command.
- [var time: CMTime](fadecommand/time.md)
  The time this command starts during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadecommand/duration)*