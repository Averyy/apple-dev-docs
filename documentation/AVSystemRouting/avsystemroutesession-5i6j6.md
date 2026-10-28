# AVSystemRouteSession

**Framework**: AVSystemRouting  
**Kind**: class  
**Role**: Class

An object that manages a single media playback session on a remote device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@interface AVSystemRouteSession : NSObject
```

## Overview

[`AVSystemRouteSession`](./avsystemroutesession-5i6j6.md) manages a single media playback session on a remote device. Create a session to initiate playback on a connected device, communicate with a remote application, and control the lifecycle of the remote playback experience.

To use a session:

1. Create an [`AVSystemRouteSession`](./avsystemroutesession-5i6j6.md) with a URL and launch mode
2. Add the session to an [`AVSystemRoute`](./avsystemroute-9kkj3.md) using [`addSession:`](./avsystemroute-9kkj3/addsession_.md)
3. Start the session with [`startWithCompletionHandler:`](./avsystemroutesession-5i6j6/startwithcompletionhandler_.md)
4. Use the returned [`AVSystemRouteMediaSession`](./avsystemroutemediasession-4mo0j.md) to communicate with the remote device
5. Call [`stop`](./avsystemroutesession-5i6j6/stop.md) when playback ends to clean up resources

Sessions are single-use. After calling [`stop`](./avsystemroutesession-5i6j6/stop.md), the session cannot be restarted or added to another route. Create a new [`AVSystemRouteSession`](./avsystemroutesession-5i6j6.md) for each new playback.

## Reporting Playback Metadata

Report playback metadata to `MPNowPlayingInfoCenter` to ensure the system displays accurate information about the current media across a person’s devices and in system UI.

## Topics

### Instance Methods
- [- initWithURL:mode:](./avsystemroutesession-5i6j6/initwithurl_mode_.md)
  Creates a session for initiating playback on a remote device.
- [- startWithCompletionHandler:](./avsystemroutesession-5i6j6/startwithcompletionhandler_.md)
  Starts the session and initiates media playback on the remote device.
- [- stop](./avsystemroutesession-5i6j6/stop.md)
  Stops the session and terminates media playback on the remote device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Routes and sessions
- [AVSystemRoute](./avsystemroute-9kkj3.md)
  An active media route to a remote device that manages connection and communication for media playback and data exchange.
- [AVSystemRouteLaunchMode](./avsystemroutelaunchmode.md)
  The mode that determines how media playback launches on a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutesession-5i6j6)*