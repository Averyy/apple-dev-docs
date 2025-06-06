# customVideoCompositor

**Framework**: AVFoundation  
**Kind**: property

The custom video compositor.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
var customVideoCompositor: (any AVVideoCompositing)? { get }
```

#### Discussion

The custom video compositor instance that is used during image generation is accessible via this property after the value of [`videoComposition`](avplayeritem/videocomposition.md) is set to an [`AVVideoComposition`](avvideocomposition.md) instance that specifies a custom video compositor class. Any additional communication between the application and that instance of the custom video compositor, if any is required for configuration or other purposes, can only occur once that has happened.

If the value of [`videoComposition`](avplayeritem/videocomposition.md) is changed from an [`AVVideoComposition`](avvideocomposition.md) that specifies a custom video compositor class to another instance of [`AVVideoComposition`](avvideocomposition.md) that specifies the same custom video compositor class, the instance of the custom video compositor that was previously created will receive the [`renderContextChanged(_:)`](avvideocompositing/rendercontextchanged(_:).md) message and remain in use for subsequent image generation.

This property is `nil` if there is no video compositor, or if the internal video compositor is in use.

## See Also

- [var videoComposition: AVVideoComposition?](avplayeritem/videocomposition.md)
  The video composition settings to be applied during playback.
- [var seekingWaitsForVideoCompositionRendering: Bool](avplayeritem/seekingwaitsforvideocompositionrendering.md)
  A Boolean value that indicates whether the item’s timing follows the displayed video frame when seeking with a video composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/customvideocompositor)*