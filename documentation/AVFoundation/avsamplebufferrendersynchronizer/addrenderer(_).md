# addRenderer(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Adds a renderer to the list of renderers under the synchronizer’s control.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Get an AVQueuedSampleBufferRenderingReceiver from an audio or video renderer with sampleBufferReceiver() and add it to the synchronizer with addReceiver(_:) instead

## Declaration

```swift
func addRenderer(_ renderer: any AVQueuedSampleBufferRendering)
```

```objc
- (void) addRenderer:(id<AVQueuedSampleBufferRendering>) renderer;
```

## Discussion

This method can be called while [`rate`](./rate.md) is not `0.0`.

## Parameters

- `renderer`: The render to be added.

## See Also

### Managing renderers
- [var renderers: [any AVQueuedSampleBufferRendering]](./renderers.md)
  An array of queued sample buffer renderers currently attached to the synchronizer.
- [func removeRenderer(any AVQueuedSampleBufferRendering, at: CMTime, completionHandler: ((Bool) -> Void)?)](./removerenderer%28_,at,completionhandler%29.md)
  Removes a renderer from the synchronizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/addrenderer(_:))*