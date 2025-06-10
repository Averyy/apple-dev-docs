# id

**Framework**: Immersive Media Support  
**Kind**: property  
**Required**: Yes

An unique command id. Ids should be unique for the whole Immersive Media file.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var id: Int { get set }
```

## See Also

- [var duration: CMTime](presentationcommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration
- [var offset: CMTime?](presentationcommand/offset.md)
  Some commands control animations by repeating the command for the whole duration, and specifying the offset of the animation from the start time of this presentation command.
- [var time: CMTime](presentationcommand/time.md)
  The time this command starts during playback.
- [var type: PresentationCommandType](presentationcommand/type.md)
  The command type. See [`PresentationCommandType`](presentationcommandtype.md) for the current set of valid command types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationcommand/id)*