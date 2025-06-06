# flush()

**Framework**: AVFoundation  
**Kind**: method

Instructs the layer to discard any enqueued sample buffers that are pending.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func flush()
```

#### Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`flush()`](avqueuedsamplebufferrendering/flush().md) on the [`sampleBufferRenderer`](avsamplebufferdisplaylayer/samplebufferrenderer.md) instead.

Because it’s not possible to determine which sample buffers have been decoded, the next frame passed to [`enqueue(_:)`](avsamplebufferdisplaylayer/enqueue(_:).md) should be an IDR frame (also known as a key frame or sync sample).

## See Also

- [func flushAndRemoveImage()](avsamplebufferdisplaylayer/flushandremoveimage.md)
  Instructs the layer to discard pending enqueued sample buffers and remove any currently displayed image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/flush())*