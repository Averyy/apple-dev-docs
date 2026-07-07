# started(application:playbackControl:session:)

**Framework**: Media Device  
**Kind**: method

Notifies the system that a remote application has successfully started on the target device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func started<T>(application applicationIdentifier: String?, playbackControl: T, session: MediaOutputSession) where T : AVPlaybackUserInterfaceControllable
```

#### Discussion

Call this function when your extension has successfully launched or connected to an application on the remote device and is ready to begin media playback. This indicates that the session has been established and the remote application is prepared to receive media content or playback commands.

This function should be called after the following conditions are met:

- The connection to the remote device has been established
- The remote application has been launched or awakened
- The playback interface is ready to accept commands
- Any necessary authentication or session initialization has completed

After calling this function, the system will be able to route media playback to the device and provide playback controls through the `playbackControl` interface.

> ❗ **Important**: Call this function on the main actor to ensure thread-safe state updates.

> **Note**: [`sessionFailed(_:error:)`](mediadeviceroutingmanager/sessionfailed(_:error:).md)

> **Note**: `AVPlaybackUserInterfaceControllable`

## Parameters

- `applicationIdentifier`: A unique identifier for the application running on the remote device. For a default media playback experience on the remote device, use `nil`.
- `playbackControl`: An object conforming to `AVPlaybackUserInterfaceControllable` that provides playback control capabilities (play, pause, seek, etc.) for the remote session.
- `session`: The [`MediaOutputSession`](mediaoutputsession.md) associated with this playback session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/started(application:playbackcontrol:session:))*