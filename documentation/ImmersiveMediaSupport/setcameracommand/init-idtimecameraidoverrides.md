# init(id:time:cameraID:overrides:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a command with a specific ID, cameraID, start time and override parameters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(id: Int, time: CMTime, cameraID: String, overrides: SetCameraCommand.Overrides?)
```

## Parameters

- `id`: The unique ID of this command.
- `time`: The time for this command to start during playback.
- `cameraID`: The `cameraID` associated with this command.
- `overrides`: The override parameters for the camera


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand/init(id:time:cameraid:overrides:))*