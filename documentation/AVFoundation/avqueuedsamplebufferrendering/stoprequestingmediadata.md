# stopRequestingMediaData()

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Cancels any current [`requestMediaDataWhenReady(on:using:)`](avqueuedsamplebufferrendering/requestmediadatawhenready(on:using:).md) call.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func stopRequestingMediaData()
```

#### Discussion

Always pair a call to [`requestMediaDataWhenReady(on:using:)`](avqueuedsamplebufferrendering/requestmediadatawhenready(on:using:).md) with this method. You can call this method from inside or outside of the requesting method’s block parameter.

## See Also

- [var isReadyForMoreMediaData: Bool](avqueuedsamplebufferrendering/isreadyformoremediadata.md)
  A Boolean value that indicates whether the receiver is able to accept more sample buffers.
- [func enqueue(CMSampleBuffer)](avqueuedsamplebufferrendering/enqueue(_:).md)
  Sends a sample buffer to the queue for rendering.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](avqueuedsamplebufferrendering/requestmediadatawhenready(on:using:).md)
  Tells the target to invoke a client-supplied block in order to gather sample buffers for playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/stoprequestingmediadata())*