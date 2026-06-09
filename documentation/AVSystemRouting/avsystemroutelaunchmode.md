# AVSystemRouteLaunchMode

**Framework**: AVSystemRouting  
**Kind**: enum

The mode that determines how media playback launches on a remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum AVSystemRouteLaunchMode
```

#### Overview

Use this enumeration with [`initWithURL:mode:`](avsystemroutesession-5i6j6/initwithurl:mode:.md) to control how media playback is initiated on the remote device. The launch mode determines whether your app launches its counterpart on the remote device, or uses a system-provided media player.

## Topics

### Enumeration Cases
- [AVSystemRouteLaunchMode.application](avsystemroutelaunchmode/application.md)
  Launches the corresponding application on the remote device.
- [AVSystemRouteLaunchMode.player](avsystemroutelaunchmode/player.md)
  Launches the system’s built-in media player on the remote device.
### Initializers
- [init?(rawValue: Int)](avsystemroutelaunchmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVSystemRoute](avsystemroute-5s2um.md)
  An active media route to a remote device that manages connection and communication for media playback and data exchange.
- [class AVSystemRouteSession](avsystemroutesession-gp78.md)
  An object that manages a single media playback session on a remote device.
- [AVSystemRoute.LaunchMode](avsystemroute-5s2um/launchmode.md)
  The mode that determines how media playback launches on a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutelaunchmode)*