# removeRenderer(_:at:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes a renderer from the synchronizer.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Use removeReceiver(_:at:) instead

## Declaration

```swift
func removeRenderer(_ renderer: any AVQueuedSampleBufferRendering, at time: CMTime, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

```swift
func removeRenderer(_ renderer: any AVQueuedSampleBufferRendering, at time: CMTime) async -> Bool
```

```objc
- (void) removeRenderer:(id<AVQueuedSampleBufferRendering>) renderer atTime:(CMTime) time completionHandler:(void (^)(BOOL didRemoveRenderer)) completionHandler;
```

#### Discussion

This method removes the renderer asynchronously. The method can be called more than once, with a subsequent scheduled removal replacing a previously scheduled removal. This method can be called while [`rate`](./rate.md) is not `0.0`.

Clients may provide an optional `completionHandler` to be notified when the scheduled removal is complete. If provided, the completion handler will always be called with the following values for `didRemoveRenderer`:

- If the renderer has not been added to this synchronizer, `didRemoveRenderer` is `NO`.
- If the removal of a particular renderer is scheduled after the same renderer’s removal was previous scheduled but not yet occurred, the previously scheduled removal’s completion handler is and `didRemoveRenderer` set to `NO`.
- When the renderer is removed due to a scheduled removal, the completion handler is called and `didRemoveRenderer` set to YES.

## Parameters

- `renderer`: 
- `time`: The time on the timebase’s timeline at which the renderer should be removed. If the time is in the past, the renderer is immediately removed.
- `completionHandler`: An optional block to invoke when the renderer is removed from the synchronizer. The block takes one argument:

  - **didRemoveRenderer**: A Boolean value indicating the whether the renderer was removed.

## See Also

### Managing renderers
- [var renderers: [any AVQueuedSampleBufferRendering]](./renderers.md)
  An array of queued sample buffer renderers currently attached to the synchronizer.
- [func addRenderer(any AVQueuedSampleBufferRendering)](./addrenderer%28_%29.md)
  Adds a renderer to the list of renderers under the synchronizer’s control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/removerenderer(_:at:completionhandler:))*