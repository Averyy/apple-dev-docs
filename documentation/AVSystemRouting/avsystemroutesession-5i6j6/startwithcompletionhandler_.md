# startWithCompletionHandler:

**Framework**: AVSystemRouting  
**Kind**: method  
**Role**: Instance Method

Starts the session and initiates media playback on the remote device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (void) startWithCompletionHandler:(void (^)(NSError *launchError, AVSystemRouteMediaSession *mediaSession)) completionHandler;
```

#### Discussion

Call this method to begin the playback session after adding it to an [`AVSystemRoute`](../avsystemroute-9kkj3.md). The session uses the URL and launch mode specified during initialization to start playback on the remote device.

When using `AVSystemRouteLaunchMode/application`, your app must declare supported protocol identifiers in the `MDESupportedProtocols` key in your `Info.plist` file. These identifiers enable the system to establish communication between your app and its counterpart on the remote device.

After a successful launch with `AVSystemRouteLaunchMode/application`, the returned [`AVSystemRouteMediaSession`](../avsystemroutemediasession-4mo0j.md) provides access to a [`dataChannel`](../avsystemroutemediasession-4mo0j/datachannel.md) and a [`playbackControl`](../avsystemroutemediasession-4mo0j/playbackcontrol.md). Use these objects to send playback commands, state updates, or custom messages between your app and the remote application.

Report playback metadata to `MPNowPlayingInfoCenter` to ensure the system displays accurate information about the current media across a person’s devices.

> ❗ **Important**: Call [`stop`](./stop.md) when playback ends to properly clean up the remote session.

> **Note**: This method operates asynchronously. The completion handler may be called on a background queue, so dispatch to the main queue if you need to update UI.

## Parameters

- `completionHandler`: A completion handler called when the launch operation completes. The handler receives two parameters: - `launchError`: An error object if the launch failed, or `nil` on success. - `mediaSession`: A media session object for communicating with the remote device. Access its [`dataChannel`](../avsystemroutemediasession-4mo0j/datachannel.md) property to send and receive data between your app and the remote application. Access its [`playbackControl`](../avsystemroutemediasession-4mo0j/playbackcontrol.md) property to send and receive playback commands between your app and the remote application. For `AVSystemRouteLaunchMode/player`, [`dataChannel`](../avsystemroutemediasession-4mo0j/datachannel.md) is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutesession-5i6j6/startwithcompletionhandler:)*