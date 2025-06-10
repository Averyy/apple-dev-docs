# offset

**Framework**: Immersive Media Support  
**Kind**: property

Not used - setCamera commands don’t use offsets.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var offset: CMTime?
```

## See Also

- [var cameraID: String](setcameracommand/cameraid.md)
  The cameraID to be used for the duration of this command.
- [var duration: CMTime](setcameracommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration
- [var id: Int](setcameracommand/id.md)
  An unique command id. Ids should be unique for the whole Immersive Media file.
- [var time: CMTime](setcameracommand/time.md)
  The time this command starts during playback.
- [var type: PresentationCommandType](setcameracommand/type.md)
  The command type (.setCamera).


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand/offset)*