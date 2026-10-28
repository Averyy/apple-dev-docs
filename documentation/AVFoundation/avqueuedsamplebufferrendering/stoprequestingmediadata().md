# stopRequestingMediaData()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Cancels any current [`requestMediaDataWhenReady(on:using:)`](./requestmediadatawhenready%28on,using%29.md) call.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

## Declaration

```swift
func stopRequestingMediaData()
```

```objc
- (void) stopRequestingMediaData;
```

## Discussion

Always pair a call to [`requestMediaDataWhenReady(on:using:)`](./requestmediadatawhenready%28on,using%29.md) with this method. You can call this method from inside or outside of the requesting method’s block parameter.

## See Also

### Requesting media
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates whether the receiver is able to accept more sample buffers.
- [func enqueue(CMSampleBuffer)](./enqueue%28_%29.md)
  Sends a sample buffer to the queue for rendering.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](./requestmediadatawhenready%28on,using%29.md)
  Tells the target to invoke a client-supplied block in order to gather sample buffers for playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/stoprequestingmediadata())*