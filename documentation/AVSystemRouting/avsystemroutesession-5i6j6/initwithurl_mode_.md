# initWithURL:mode:

**Framework**: AVSystemRouting  
**Kind**: method  
**Role**: Instance Method

Creates a session for initiating playback on a remote device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (instancetype) initWithURL:(NSURL *) url mode:(AVSystemRouteLaunchMode) mode;
```

## Discussion

Initialize a session with the media URL and launch mode before adding it to an [`AVSystemRoute`](../avsystemroute-9kkj3.md). The URL and mode determine how the remote device handles playback — either by launching your app’s counterpart or using the system’s built-in media player.

> **Note**: After creating a session, you must add it to an [`AVSystemRoute`](../avsystemroute-9kkj3.md) using [`addSession:`](../avsystemroute-9kkj3/addsession_.md) before calling [`startWithCompletionHandler:`](./startwithcompletionhandler_.md).

## Parameters

- `url`: The URL identifying the media content to play. This URL is passed to the remote application or player. For application mode, your remote application receives this URL to handle appropriately (for example, to navigate to specific content). For player mode, the system uses this URL to load media directly.
- `mode`: The launch mode determining whether to start your app’s counterpart (`AVSystemRouteLaunchMode/application`) or the system media player (`AVSystemRouteLaunchMode/player`) on the remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutesession-5i6j6/initwithurl:mode:)*