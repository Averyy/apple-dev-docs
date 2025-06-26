# id

**Framework**: Immersive Media Support  
**Kind**: property

A unique command id. Ids should be unique for the whole Immersive Media file.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var id: Int { get }
```

## See Also

- [var duration: CMTime](shotflopcommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration.
- [var offset: CMTime?](shotflopcommand/offset.md)
  Some commands control animations by repeating the command for the whole duration, and specifying the offset of the animation from the start time of this presentation command.
- [var time: CMTime](shotflopcommand/time.md)
  The time this command starts during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/shotflopcommand/id)*