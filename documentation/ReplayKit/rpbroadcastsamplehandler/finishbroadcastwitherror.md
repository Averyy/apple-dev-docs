# finishBroadcastWithError(_:)

**Framework**: ReplayKit  
**Kind**: method

Stops the broadcast and passes an error back to the broadcasting app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func finishBroadcastWithError(_ error: any Error)
```

#### Discussion

Call this method in your sample handler when it cannot proceed due to an error.

## Parameters

- `error`: An NSError object that is passed back to the broadcasting app through the   method.

## See Also

- [func broadcastStarted(withSetupInfo: [String : NSObject]?)](rpbroadcastsamplehandler/broadcaststarted(withsetupinfo:).md)
  Perform any required actions after starting a live broadcast.
- [func broadcastPaused()](rpbroadcastsamplehandler/broadcastpaused.md)
  Perform any required actions after a live broadcast is paused.
- [func broadcastResumed()](rpbroadcastsamplehandler/broadcastresumed.md)
  Perform any required actions after a live broadcast is resumed.
- [func broadcastFinished()](rpbroadcastsamplehandler/broadcastfinished.md)
  Perform any required actions after a live broadcast is finished.
- [func broadcastAnnotated(withApplicationInfo: [AnyHashable : Any])](rpbroadcastsamplehandler/broadcastannotated(withapplicationinfo:).md)
  Perform any required actions after starting a live broadcast.
- [let RPApplicationInfoBundleIdentifierKey: String](rpapplicationinfobundleidentifierkey.md)
  The key to retrieve the app’s bundle identifier from the user-information dictionary.
- [func processSampleBuffer(CMSampleBuffer, with: RPSampleBufferType)](rpbroadcastsamplehandler/processsamplebuffer(_:with:).md)
  Processes video and audio data as it becomes available during a live broadcast.
- [let RPVideoSampleOrientationKey: String](rpvideosampleorientationkey.md)
  The sample attachment key that describes the video orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/finishbroadcastwitherror(_:))*