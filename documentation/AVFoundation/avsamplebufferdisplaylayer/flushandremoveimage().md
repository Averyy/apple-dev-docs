# flushAndRemoveImage()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Instructs the layer to discard pending enqueued sample buffers and remove any currently displayed image.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 10.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use sampleBufferRenderer's flushWithRemovalOfDisplayedImage:completionHandler: instead

## Declaration

```swift
func flushAndRemoveImage()
```

```objc
- (void) flushAndRemoveImage;
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`flush(removingDisplayedImage:completionHandler:)`](../avsamplebuffervideorenderer/flush%28removingdisplayedimage,completionhandler%29.md) on the [`sampleBufferRenderer`](./samplebufferrenderer.md) instead.

It is not possible to determine which sample buffers have been decoded, so the next frame passed to [`enqueue(_:)`](./enqueue%28_%29.md) should be an IDR frame (also known as a key frame or sync sample).

## See Also

### Flushing sample buffers
- [func flush()](./flush%28%29.md)
  Instructs the layer to discard any enqueued sample buffers that are pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/flushandremoveimage())*