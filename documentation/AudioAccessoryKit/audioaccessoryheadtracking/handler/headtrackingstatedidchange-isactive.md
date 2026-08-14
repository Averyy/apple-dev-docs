# headTrackingStateDidChange(isActive:)

**Framework**: AudioAccessoryKit  
**Kind**: method  
**Required**: Yes

Called when the user-facing Head Tracking state for this accessory changes (e.g. via Settings or Control Center).

**Availability**:
- iOS 27.0+ (Beta)

## Declaration

```swift
func headTrackingStateDidChange(isActive: Bool)
```

#### Discussion

Implementations should start or stop sampling the accessory’s IMU based on the new state.

## Parameters

- `isActive`: `true` when head tracking is enabled and the extension should stream IMU samples via `Session.sendDataToAudioExtension(_:)`; `false` when head tracking is disabled and the extension should stop sampling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/audioaccessoryheadtracking/handler/headtrackingstatedidchange(isactive:))*