# outputSequenceWasRestarted:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Invoked when the output is commencing a new sequence.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```objc
- (void) outputSequenceWasRestarted:(AVPlayerItemSampleBufferOutput *) output;
```

#### Discussion

This method is invoked after seeks and changes in playback direction. If you are maintaining any queued future samples previously copied, it may be appropriate to discard these upon receiving this message.

Note that delivery of this message may race with calls to `-copyNextSampleBuffer`.

## See Also

### Responding to output events
- [- outputMediaDataAvailable:](./outputmediadataavailable_.md)
  Invoked when the output becomes ready to deliver a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutputdelegate/outputsequencewasrestarted:)*