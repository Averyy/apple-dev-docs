# init(id:time:cameraID:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes a `setCamera` command with a specific cameraID and start time.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(id: Int, time: CMTime, cameraID: String)
```

## Parameters

- `id`: The unique id of this command.
- `time`: The time for this command to be activated during playback.
- `cameraID`: The cameraID associated with this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand/init(id:time:cameraid:))*