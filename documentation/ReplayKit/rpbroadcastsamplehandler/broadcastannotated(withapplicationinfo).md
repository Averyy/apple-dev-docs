# broadcastAnnotated(withApplicationInfo:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Perform any required actions after starting a live broadcast.

**Availability**:
- iOS 11.2+ - Deprecated in 27.0
- iPadOS 11.2+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
func broadcastAnnotated(withApplicationInfo applicationInfo: [AnyHashable : Any])
```

```objc
- (void) broadcastAnnotatedWithApplicationInfo:(NSDictionary *) applicationInfo;
```

## Parameters

- `applicationInfo`: A dictionary containing information about the first application opened or used buring the broadcast.

## See Also

### Handling Sample Buffer Clips
- [func broadcastStarted(withSetupInfo: [String : NSObject]?)](./broadcaststarted%28withsetupinfo%29.md)
  Perform any required actions after starting a live broadcast.
- [func broadcastPaused()](./broadcastpaused%28%29.md)
  Perform any required actions after a live broadcast is paused.
- [func broadcastResumed()](./broadcastresumed%28%29.md)
  Perform any required actions after a live broadcast is resumed.
- [func broadcastFinished()](./broadcastfinished%28%29.md)
  Perform any required actions after a live broadcast is finished.
- [let RPApplicationInfoBundleIdentifierKey: String](../rpapplicationinfobundleidentifierkey.md)
  The key to retrieve the app’s bundle identifier from the user-information dictionary.
- [func processSampleBuffer(CMSampleBuffer, with: RPSampleBufferType)](./processsamplebuffer%28_,with%29.md)
  Processes video and audio data as it becomes available during a live broadcast.
- [let RPVideoSampleOrientationKey: String](../rpvideosampleorientationkey.md)
  The sample attachment key that describes the video orientation.
- [func finishBroadcastWithError(any Error)](./finishbroadcastwitherror%28_%29.md)
  Stops the broadcast and passes an error back to the broadcasting app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/broadcastannotated(withapplicationinfo:))*