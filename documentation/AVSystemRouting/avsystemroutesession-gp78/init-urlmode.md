# init(url:mode:)

**Framework**: AVSystemRouting  
**Kind**: init

Creates a session for initiating playback on a remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(url: URL, mode: AVSystemRoute.LaunchMode)
```

#### Discussion

Initialize a session with the media URL and launch mode before adding it to an [`AVSystemRoute`](avsystemroute-5s2um.md). The URL and mode determine how the remote device handles playback — either by launching your app’s counterpart or using the system’s built-in media player.

> **Note**: After creating a session, you must add it to an [`AVSystemRoute`](avsystemroute-5s2um.md) using [`addSession(_:)`](avsystemroute-5s2um/addsession(_:).md) before calling [`start()`](avsystemroutesession-gp78/start().md).

## Parameters

- `url`: The URL identifying the media content to play. This URL is passed to the remote application or player. For application mode, your remote application receives this URL to handle appropriately (for example, to navigate to specific content). For player mode, the system uses this URL to load media directly.
- `mode`: The launch mode determining whether to start your app’s counterpart ([`AVSystemRoute.LaunchMode.application`](avsystemroute-5s2um/launchmode/application.md)) or the system media player ([`AVSystemRoute.LaunchMode.player`](avsystemroute-5s2um/launchmode/player.md)) on the remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutesession-gp78/init(url:mode:))*