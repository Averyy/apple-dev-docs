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

- [var cameraID: String](setcameracommand/cameraid.md)
  The cameraID to be used for the duration of this command.
- [var duration: CMTime](setcameracommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration
- [var id: Int](setcameracommand/id.md)
  A unique command id. Ids should be unique for the whole Immersive Media file.
- [var offset: CMTime?](setcameracommand/offset.md)
  Not used - setCamera commands don’t use offsets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand/time)*