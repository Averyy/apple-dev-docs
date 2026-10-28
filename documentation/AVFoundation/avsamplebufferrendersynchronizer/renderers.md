# renderers

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of queued sample buffer renderers currently attached to the synchronizer.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Accessing non-Sendable renderers concurrently risks causing data races

## Declaration

```swift
var renderers: [any AVQueuedSampleBufferRendering] { get }
```

```objc
@property (atomic, readonly) NSArray<__kindof id<AVQueuedSampleBufferRendering>> * renderers;
```

## Discussion

This property includes all renderers that have been added to the synchronizer and haven’t been removed, including renderers that have been scheduled for removal, but have yet to be removed. This property is not KVO observable.

## See Also

### Managing renderers
- [func addRenderer(any AVQueuedSampleBufferRendering)](./addrenderer%28_%29.md)
  Adds a renderer to the list of renderers under the synchronizer’s control.
- [func removeRenderer(any AVQueuedSampleBufferRendering, at: CMTime, completionHandler: ((Bool) -> Void)?)](./removerenderer%28_,at,completionhandler%29.md)
  Removes a renderer from the synchronizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/renderers)*