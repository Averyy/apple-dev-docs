# mediaServicesWereLostNotification

**Framework**: AVFAudio  
**Kind**: property

A notification the system posts when it terminates the media server.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let mediaServicesWereLostNotification: NSNotification.Name
```

#### Discussion

The system posts this notification when the media server first becomes unavailable. Most apps don’t need to subscribe to this notification and should instead subscribe to the [`mediaServicesWereResetNotification`](avaudiosession/mediaserviceswereresetnotification.md) notification. However, you can use this notification as a cue to take any appropriate steps to handle requests that come in before the server restarts.

This notification has no [`userInfo`](https://developer.apple.com/documentation/Foundation/NSNotification/userInfo) dictionary.

The system posts this notification on the main thread.

## See Also

- [class let mediaServicesWereResetNotification: NSNotification.Name](avaudiosession/mediaserviceswereresetnotification.md)
  A notification the system posts when the media server restarts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mediaserviceswerelostnotification)*