# broadcastFinished()

**Framework**: ReplayKit  
**Kind**: method

Perform any required actions after a live broadcast is finished.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func broadcastFinished()
```

#### Discussion

ReplayKit calls this method when the the broadcasting app calls its [`finishBroadcast(handler:)`](rpbroadcastcontroller/finishbroadcast(handler:).md) method.

## See Also

- [func broadcastStarted(withSetupInfo: [String : NSObject]?)](rpbroadcastsamplehandler/broadcaststarted(withsetupinfo:).md)
  Perform any required actions after starting a live broadcast.
- [func broadcastPaused()](rpbroadcastsamplehandler/broadcastpaused.md)
  Perform any required actions after a live broadcast is paused.
- [func broadcastResumed()](rpbroadcastsamplehandler/broadcastresumed.md)
  Perform any required actions after a live broadcast is resumed.
- [func broadcastAnnotated(withApplicationInfo: [AnyHashable : Any])](rpbroadcastsamplehandler/broadcastannotated(withapplicationinfo:).md)
  Perform any required actions after starting a live broadcast.
- [let RPApplicationInfoBundleIdentifierKey: String](rpapplicationinfobundleidentifierkey.md)
  The key to retrieve the app’s bundle identifier from the user-information dictionary.
- [func processSampleBuffer(CMSampleBuffer, with: RPSampleBufferType)](rpbroadcastsamplehandler/processsamplebuffer(_:with:).md)
  Processes video and audio data as it becomes available during a live broadcast.
- [let RPVideoSampleOrientationKey: String](rpvideosampleorientationkey.md)
  The sample attachment key that describes the video orientation.
- [func finishBroadcastWithError(any Error)](rpbroadcastsamplehandler/finishbroadcastwitherror(_:).md)
  Stops the broadcast and passes an error back to the broadcasting app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/broadcastfinished())*