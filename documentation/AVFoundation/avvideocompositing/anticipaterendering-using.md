# anticipateRendering(using:)

**Framework**: AVFoundation  
**Kind**: method

Informs a custom video compositor about upcoming rendering requests.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func anticipateRendering(using renderHint: AVVideoCompositionRenderHint)
```

#### Discussion

In this method, the compositor can load composition resources, such as overlay images, that will be needed in the anticipated rendering time range.

Unlike the [`startRequest(_:)`](avvideocompositing/startrequest(_:).md) method, which is invoked only when the frame compositing is necessary, this method is typically called every frame duration. It allows the custom compositor to load and unload a composition resource such as overlay images at an appropriate time.

In forward playback, the render hint’s [`startCompositionTime`](avvideocompositionrenderhint/startcompositiontime.md) is less than its [`endCompositionTime`](avvideocompositionrenderhint/endcompositiontime.md). In reverse playback, its [`endCompositionTime`](avvideocompositionrenderhint/endcompositiontime.md) is less than its [`startCompositionTime`](avvideocompositionrenderhint/startcompositiontime.md). For seeking, the two values are equivalent, which means the upcoming composition request time range is unknown.

This method is guaranteed to be called before [`startRequest(_:)`](avvideocompositing/startrequest(_:).md) for a given composition time.

This method is synchronous. Make sure that your implementation returns quickly to ensure that playback doesn’t stall and cause frame drops.

## Parameters

- `renderHint`: Information about the upcoming composition requests.

## See Also

- [func prerollForRendering(using: AVVideoCompositionRenderHint)](avvideocompositing/prerollforrendering(using:).md)
  Tells a custom video compositor to perform any work in the prerolling phase.
- [class AVVideoCompositionRenderHint](avvideocompositionrenderhint.md)
  Information about upcoming composition requests, such as composition start time and end time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositing/anticipaterendering(using:))*