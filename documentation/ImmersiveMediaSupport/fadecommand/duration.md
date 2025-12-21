# duration

**Framework**: Immersive Media Support  
**Kind**: property

The duration of the command.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var duration: CMTime
```

## See Also

- [var color: simd_float3](fadecommand/color.md)
  The fade color value ranging from `0.0` to `1.0` for each color channel representing RGB color space. If the color is set to black, and the direction is `in`, then it fades from black to the video frame.
- [var direction: FadeCommand.FadeDirection](fadecommand/direction.md)
  Fade direction for this command instance.
- [var id: Int](fadecommand/id.md)
  A unique command ID for the entire immersive media file.
- [var offset: CMTime?](fadecommand/offset.md)
  The offset from the start time of this command.
- [var time: CMTime](fadecommand/time.md)
  The time this command starts during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadecommand/duration)*