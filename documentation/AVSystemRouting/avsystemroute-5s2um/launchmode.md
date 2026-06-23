# AVSystemRoute.LaunchMode

**Framework**: AVSystemRouting  
**Kind**: enum

The mode that determines how media playback launches on a remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum LaunchMode
```

#### Overview

Use this enumeration with [`init(url:mode:)`](avsystemroutesession-gp78/init(url:mode:).md) to control how media playback is initiated on the remote device. The launch mode determines whether your app launches its counterpart on the remote device, or uses a system-provided media player.

## Topics

### Enumeration Cases
- [AVSystemRoute.LaunchMode.application](avsystemroute-5s2um/launchmode/application.md)
  Launches the corresponding application on the remote device.
- [AVSystemRoute.LaunchMode.player](avsystemroute-5s2um/launchmode/player.md)
  Launches the system’s built-in media player on the remote device.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVSystemRoute](avsystemroute-5s2um.md)
  An active media route to a remote device that manages connection and communication for media playback and data exchange.
- [class AVSystemRouteSession](avsystemroutesession-gp78.md)
  An object that manages a single media playback session on a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-5s2um/launchmode)*