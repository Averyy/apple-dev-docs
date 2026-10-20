# AVSampleBufferVideoRenderer.Receiver.RenderingEvent.didFailToDecode(_:)

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

Indicates that the renderer failed to decode one or more previously enqueued sample buffers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case didFailToDecode([any Error])
```

## See Also

### Rendering events
- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.requiresFlushToResumeDecoding(_:)](./requiresflushtoresumedecoding%28_%29.md)
  The Receiver requires a flush to continue enqueuing samples.
- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.failed(_:)](./failed%28_%29.md)
  Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingevent/didfailtodecode(_:))*