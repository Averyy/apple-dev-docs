# addRenderer(_:)

**Framework**: AVFoundation  
**Kind**: method

Adds a renderer to the list of renderers under the synchronizer’s control.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func addRenderer(_ renderer: any AVQueuedSampleBufferRendering)
```

#### Discussion

This method can be called while [`rate`](avsamplebufferrendersynchronizer/rate.md) is not `0.0`.

## Parameters

- `renderer`: The render to be added.

## See Also

- [var renderers: [any AVQueuedSampleBufferRendering]](avsamplebufferrendersynchronizer/renderers.md)
  An array of queued sample buffer renderers currently attached to the synchronizer.
- [func removeRenderer(any AVQueuedSampleBufferRendering, at: CMTime, completionHandler: ((Bool) -> Void)?)](avsamplebufferrendersynchronizer/removerenderer(_:at:completionhandler:).md)
  Removes a renderer from the synchronizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/addrenderer(_:))*