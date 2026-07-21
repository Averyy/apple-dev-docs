# sendDataToAudioExtension(_:)

**Framework**: AudioAccessoryKit  
**Kind**: method

Forward a frame of IMU sensor data from the accessory to the Spatial Audio renderer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
final func sendDataToAudioExtension(_ data: Data) throws
```

#### Discussion

> **Note**: `AudioAccessoryError.invalidDataSize` if `data` is empty or larger than 70 bytes; `AudioAccessoryError.notActivated` if the session is not currently active.

## Parameters

- `data`: The raw sensor frame as received from the accessory. Must be 1–70 bytes; otherwise `AudioAccessoryError.invalidDataSize` is thrown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/audioaccessoryheadtracking/session/senddatatoaudioextension(_:))*