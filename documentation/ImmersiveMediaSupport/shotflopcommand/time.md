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

- [var duration: CMTime](shotflopcommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration.
- [var id: Int](shotflopcommand/id.md)
  A unique command id. Ids should be unique for the whole Immersive Media file.
- [var offset: CMTime?](shotflopcommand/offset.md)
  Some commands control animations by repeating the command for the whole duration, and specifying the offset of the animation from the start time of this presentation command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/shotflopcommand/time)*