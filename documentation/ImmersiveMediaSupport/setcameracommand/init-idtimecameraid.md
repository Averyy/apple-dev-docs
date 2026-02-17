# init(id:time:cameraID:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a command with a specific ID, cameraID and start time.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(id: Int, time: CMTime, cameraID: String)
```

## Parameters

- `id`: The unique ID of this command.
- `time`: The time for this command to start during playback.
- `cameraID`: The   associated with this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand/init(id:time:cameraid:))*