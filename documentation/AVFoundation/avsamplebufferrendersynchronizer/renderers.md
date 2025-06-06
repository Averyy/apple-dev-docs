# renderers

**Framework**: AVFoundation  
**Kind**: property

An array of queued sample buffer renderers currently attached to the synchronizer.

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
var renderers: [any AVQueuedSampleBufferRendering] { get }
```

#### Discussion

This property includes all renderers that have been added to the synchronizer and haven’t been removed, including renderers that have been scheduled for removal, but have yet to be removed. This property is not KVO observable.

## See Also

- [func addRenderer(any AVQueuedSampleBufferRendering)](avsamplebufferrendersynchronizer/addrenderer(_:).md)
  Adds a renderer to the list of renderers under the synchronizer’s control.
- [func removeRenderer(any AVQueuedSampleBufferRendering, at: CMTime, completionHandler: ((Bool) -> Void)?)](avsamplebufferrendersynchronizer/removerenderer(_:at:completionhandler:).md)
  Removes a renderer from the synchronizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/renderers)*