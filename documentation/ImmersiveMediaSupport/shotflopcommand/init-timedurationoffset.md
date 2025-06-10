# init(time:duration:offset:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes a shotFlop command for a certain time, duration and offset.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(time: CMTime, duration: CMTime, offset: CMTime? = nil)
```

## Parameters

- `time`: The time for this command to be activated during playback.
- `duration`: The duration of the shotFlop during playback.
- `offset`: The offset from the start time of this command. This parameter is usually unused and let in control of a PresentationDescriptorReader.

## See Also

- [init(from: any Decoder) throws](shotflopcommand/init(from:).md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/shotflopcommand/init(time:duration:offset:))*