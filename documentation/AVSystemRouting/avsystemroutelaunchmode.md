# AVSystemRouteLaunchMode

**Framework**: AVSystemRouting  
**Kind**: enum  
**Role**: Enumeration

The mode that determines how media playback launches on a remote device.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst

## Declaration

```c
enum AVSystemRouteLaunchMode : NSInteger;
```

#### Overview

Use this enumeration with [`initWithURL:mode:`](./avsystemroutesession-5i6j6/initwithurl_mode_.md) to control how media playback is initiated on the remote device. The launch mode determines whether your app launches its counterpart on the remote device, or uses a system-provided media player.

## Topics

### Enumeration Cases
- [AVSystemRouteLaunchModeApplication](./avsystemroutelaunchmode/avsystemroutelaunchmodeapplication.md)
  Launches the corresponding application on the remote device.
- [AVSystemRouteLaunchModePlayer](./avsystemroutelaunchmode/avsystemroutelaunchmodeplayer.md)
  Launches the system’s built-in media player on the remote device.

## See Also

### Routes and sessions
- [AVSystemRoute](./avsystemroute-9kkj3.md)
  An active media route to a remote device that manages connection and communication for media playback and data exchange.
- [AVSystemRouteSession](./avsystemroutesession-5i6j6.md)
  An object that manages a single media playback session on a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutelaunchmode)*