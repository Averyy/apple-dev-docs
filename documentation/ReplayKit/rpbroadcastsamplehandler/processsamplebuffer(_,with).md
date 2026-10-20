# processSampleBuffer(_:with:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Processes video and audio data as it becomes available during a live broadcast.

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
func processSampleBuffer(_ sampleBuffer: CMSampleBuffer, with sampleBufferType: RPSampleBufferType)
```

```objc
- (void) processSampleBuffer:(CMSampleBufferRef) sampleBuffer withType:(RPSampleBufferType) sampleBufferType;
```

#### Discussion

This method handles buffers of all sample buffer types throughout each broadcast. If no audio is available — for example, if the microphone isn’t capturing input — ReplayKit provides audio buffers whose samples represent continuous silence.

ReplayKit provides sample buffers sequentially. After invoking this method with a sample buffer, ReplayKit won’t invoke the method again for any sample buffer type until the current invocation returns.

The sample buffer passed to this method is available only until the method returns. You shouldn’t keep a reference to the sample buffer after the method returns.

## Parameters

- `sampleBuffer`: A [`CMSampleBuffer`](../../CoreMedia/cmsamplebuffer.md) object containing either audio or video data.
- `sampleBufferType`: An [`RPSampleBufferType`](../rpsamplebuffertype.md) identifying the media type of the recorded sample.

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
- [let RPVideoSampleOrientationKey: String](../rpvideosampleorientationkey.md)
  The sample attachment key that describes the video orientation.
- [func finishBroadcastWithError(any Error)](./finishbroadcastwitherror%28_%29.md)
  Stops the broadcast and passes an error back to the broadcasting app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/processsamplebuffer(_:with:))*