# broadcastFinished()

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Perform any required actions after a live broadcast is finished.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
func broadcastFinished()
```

```objc
- (void) broadcastFinished;
```

## Discussion

ReplayKit calls this method when the the broadcasting app calls its [`finishBroadcast(handler:)`](../rpbroadcastcontroller/finishbroadcast%28handler%29.md) method.

## See Also

### Handling Sample Buffer Clips
- [func broadcastStarted(withSetupInfo: [String : NSObject]?)](./broadcaststarted%28withsetupinfo%29.md)
  Perform any required actions after starting a live broadcast.
- [func broadcastPaused()](./broadcastpaused%28%29.md)
  Perform any required actions after a live broadcast is paused.
- [func broadcastResumed()](./broadcastresumed%28%29.md)
  Perform any required actions after a live broadcast is resumed.
- [func broadcastAnnotated(withApplicationInfo: [AnyHashable : Any])](./broadcastannotated%28withapplicationinfo%29.md)
  Perform any required actions after starting a live broadcast.
- [let RPApplicationInfoBundleIdentifierKey: String](../rpapplicationinfobundleidentifierkey.md)
  The key to retrieve the app’s bundle identifier from the user-information dictionary.
- [func processSampleBuffer(CMSampleBuffer, with: RPSampleBufferType)](./processsamplebuffer%28_,with%29.md)
  Processes video and audio data as it becomes available during a live broadcast.
- [let RPVideoSampleOrientationKey: String](../rpvideosampleorientationkey.md)
  The sample attachment key that describes the video orientation.
- [func finishBroadcastWithError(any Error)](./finishbroadcastwitherror%28_%29.md)
  Stops the broadcast and passes an error back to the broadcasting app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/broadcastfinished())*