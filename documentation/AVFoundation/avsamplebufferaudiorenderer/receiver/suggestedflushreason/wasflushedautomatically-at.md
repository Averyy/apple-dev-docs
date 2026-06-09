# AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason.wasFlushedAutomatically(at:)

**Framework**: AVFoundation  
**Kind**: case

The enqueued media data has been flushed for a reason other than a call to the `flush()` method.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case wasFlushedAutomatically(at: CMTime)
```

#### Discussion

The renderer may flush enqueued media data when the user routes playback to a new destination.  The renderer may also flush enqueued media data when the playback rate of the attached render synchronizer is changed (e.g. 1.0 -> 2.0 or 1.0 -> 0.0 -> 2.0), however no flush will occur for normal pauses (non-zero -> 0.0) and resumes (0.0 -> same non-zero rate as before).

When an automatic flush occurs, the attached render synchronizer’s timebase will remain running at its current rate.  It is typically best to respond to this event by enqueueing media data with timestamps starting at the timebase’s current time.  To the listener, this will sound similar to muting the audio for a short period of time.  If it is more desirable to ensure that all audio is played than to keep the timeline moving, you may also stop the synchronizer, set the synchronizer’s current time to the associated CMTime value of this event, start reenqueueing sample buffers with timestamps starting at that time, and restart the synchronizer.  To the listener, this will sound similar to pausing the audio for a short period of time.

The best practice is to invoke the `flush()` method, in a manner that is serialized with enqueueing sample buffers, after receiving this event and before resuming the enqueueing of sample buffers.

## See Also

- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason.outputConfigurationChanged](avsamplebufferaudiorenderer/receiver/suggestedflushreason/outputconfigurationchanged.md)
  The audio output configuration has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/suggestedflushreason/wasflushedautomatically(at:))*