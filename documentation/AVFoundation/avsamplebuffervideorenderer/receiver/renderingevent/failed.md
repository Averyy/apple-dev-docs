# AVSampleBufferVideoRenderer.Receiver.RenderingEvent.failed(_:)

**Framework**: AVFoundation  
**Kind**: case

Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case failed(any Error)
```

## See Also

- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.didFailToDecode(_:)](avsamplebuffervideorenderer/receiver/renderingevent/didfailtodecode(_:).md)
  Indicates that the renderer failed to decode one or more previously enqueued sample buffers.
- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.requiresFlushToResumeDecoding(_:)](avsamplebuffervideorenderer/receiver/renderingevent/requiresflushtoresumedecoding(_:).md)
  The Receiver requires a flush to continue enqueuing samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingevent/failed(_:))*