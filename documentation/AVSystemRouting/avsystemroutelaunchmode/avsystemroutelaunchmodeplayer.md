# AVSystemRouteLaunchModePlayer

**Framework**: AVSystemRouting  
**Kind**: case  
**Role**: Enumeration Case

Launches the system’s built-in media player on the remote device.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst

## Declaration

```c
AVSystemRouteLaunchModePlayer
```

## Discussion

Use this mode when you want to use the remote device’s built-in media player instead of launching a custom application. This provides a standardized playback experience without requiring a corresponding application to be installed on the remote device.

To support the `AVSystemRouteLaunchModePlayer` launch mode, the `MDESupportsUniversalURLPlayback` key must be set in the app’s `Info.plist` file. For example:

```xml
<key>MDESupportsUniversalURLPlayback</key>
<true/>
```

> ❗ **Important**: If `MDESupportsUniversalURLPlayback` is not set to `true`, calls to [`startWithCompletionHandler:`](../avsystemroutesession-5i6j6/startwithcompletionhandler_.md) fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutelaunchmode/avsystemroutelaunchmodeplayer)*