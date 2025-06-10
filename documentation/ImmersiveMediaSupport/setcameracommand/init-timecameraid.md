# init(time:cameraID:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes a setCamera command with a specific cameraID and start time.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(time: CMTime, cameraID: String)
```

## Parameters

- `time`: The time for this command to be activated during playback.
- `cameraID`: The cameraID associated with this command.

## See Also

- [init(from: any Decoder) throws](setcameracommand/init(from:).md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand/init(time:cameraid:))*