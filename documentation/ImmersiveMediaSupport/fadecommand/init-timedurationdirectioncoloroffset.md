# init(time:duration:direction:color:offset:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes a color fade command.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(time: CMTime, duration: CMTime, direction: FadeCommand.FadeDirection, color: simd_float3, offset: CMTime? = nil)
```

## Parameters

- `time`: The time this command starts during playback.
- `duration`: The duration of the command - this can be .zero if the command has no duration.
- `direction`: Fade direction for this command instance.
- `color`: Fade color.
- `offset`: The offset from the start time of this command. This parameter is usually unused and let in control of a PresentationDescriptorReader.

## See Also

- [init(from: any Decoder) throws](fadecommand/init(from:).md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadecommand/init(time:duration:direction:color:offset:))*