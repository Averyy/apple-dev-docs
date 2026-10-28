# broadcastStarted(withSetupInfo:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Perform any required actions after starting a live broadcast.

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
func broadcastStarted(withSetupInfo setupInfo: [String : NSObject]?)
```

```objc
- (void) broadcastStartedWithSetupInfo:(NSDictionary<NSString *,NSObject *> *) setupInfo;
```

## Discussion

ReplayKit calls this method when the the broadcasting app calls its [`startBroadcast(handler:)`](../rpbroadcastcontroller/startbroadcast%28handler%29.md) method.

## Parameters

- `setupInfo`: A dictionary supplied by the ReplayKit UI extension that contains any required setup information.

## See Also

### Handling Sample Buffer Clips
- [func broadcastPaused()](./broadcastpaused%28%29.md)
  Perform any required actions after a live broadcast is paused.
- [func broadcastResumed()](./broadcastresumed%28%29.md)
  Perform any required actions after a live broadcast is resumed.
- [func broadcastFinished()](./broadcastfinished%28%29.md)
  Perform any required actions after a live broadcast is finished.
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

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/broadcaststarted(withsetupinfo:))*