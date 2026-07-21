# playbackControl

**Framework**: AVSystemRouting  
**Kind**: property

The playback control interface for the remote session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final var playbackControl: (any AVPlaybackUserInterfaceControllable)? { get }
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)
- [Routing media to third-party devices](routing-media-to-third-party-devices.md)

#### Discussion

This property is always non-nil when obtained from a successful call to [`start()`](avsystemroutesession-gp78/start().md).

> ❗ **Important**: Always update media playback state information regularly in the playbackControl object to ensure the system displays accurate information about the current media play state across a person’s devices and in system UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutemediasession-98ioq/playbackcontrol)*