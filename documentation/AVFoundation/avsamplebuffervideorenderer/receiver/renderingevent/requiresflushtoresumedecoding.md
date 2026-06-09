# AVSampleBufferVideoRenderer.Receiver.RenderingEvent.requiresFlushToResumeDecoding(_:)

**Framework**: AVFoundation  
**Kind**: case

The Receiver requires a flush to continue enqueuing samples.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case requiresFlushToResumeDecoding((any Error)?)
```

## See Also

- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.didFailToDecode(_:)](avsamplebuffervideorenderer/receiver/renderingevent/didfailtodecode(_:).md)
  Indicates that the renderer failed to decode one or more previously enqueued sample buffers.
- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.failed(_:)](avsamplebuffervideorenderer/receiver/renderingevent/failed(_:).md)
  Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingevent/requiresflushtoresumedecoding(_:))*