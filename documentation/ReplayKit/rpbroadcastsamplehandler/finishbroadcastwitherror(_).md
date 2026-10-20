# finishBroadcastWithError(_:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Stops the broadcast and passes an error back to the broadcasting app.

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
func finishBroadcastWithError(_ error: any Error)
```

```objc
- (void) finishBroadcastWithError:(NSError *) error;
```

#### Discussion

Call this method in your sample handler when it cannot proceed due to an error.

## Parameters

- `error`: An NSError object that is passed back to the broadcasting app through the [`broadcastController(_:didFinishWithError:)`](../rpbroadcastcontrollerdelegate/broadcastcontroller%28_,didfinishwitherror%29.md) method.

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
- [func broadcastAnnotated(withApplicationInfo: [AnyHashable : Any])](./broadcastannotated%28withapplicationinfo%29.md)
  Perform any required actions after starting a live broadcast.
- [let RPApplicationInfoBundleIdentifierKey: String](../rpapplicationinfobundleidentifierkey.md)
  The key to retrieve the app’s bundle identifier from the user-information dictionary.
- [func processSampleBuffer(CMSampleBuffer, with: RPSampleBufferType)](./processsamplebuffer%28_,with%29.md)
  Processes video and audio data as it becomes available during a live broadcast.
- [let RPVideoSampleOrientationKey: String](../rpvideosampleorientationkey.md)
  The sample attachment key that describes the video orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/finishbroadcastwitherror(_:))*