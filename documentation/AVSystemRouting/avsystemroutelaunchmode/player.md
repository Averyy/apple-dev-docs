# AVSystemRouteLaunchMode.player

**Framework**: AVSystemRouting  
**Kind**: case

Launches the system’s built-in media player on the remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
case player
```

#### Discussion

Use this mode when you want to use the remote device’s built-in media player instead of launching a custom application. This provides a standardized playback experience without requiring a corresponding application to be installed on the remote device.

To support the `AVSystemRouteLaunchModePlayer` launch mode, the `MDESupportsUniversalURLPlayback` key must be set in the app’s `Info.plist` file. For example:

```xml
<key>MDESupportsUniversalURLPlayback</key>
<true/>
```

> ❗ **Important**: If `MDESupportsUniversalURLPlayback` is not set to `true`, calls to [`startWithCompletionHandler:`](avsystemroutesession-5i6j6/startwithcompletionhandler:.md) fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutelaunchmode/player)*