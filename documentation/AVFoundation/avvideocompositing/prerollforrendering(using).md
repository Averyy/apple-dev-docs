# prerollForRendering(using:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells a custom video compositor to perform any work in the prerolling phase.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func prerollForRendering(using renderHint: AVVideoCompositionRenderHint)
```

```objc
- (void) prerollForRenderingUsingHint:(AVVideoCompositionRenderHint *) renderHint;
```

## Discussion

The AVFoundation framework may perform prerolling to load media data to prime the render pipelines for smoother playback. This method is called in the prerolling phase so that the compositor can load composition resources, such as overlay images, that will be needed as soon as the playback starts.

Not all rendering scenarios use prerolling. For example, this method won’t be called during seeking.

If this method is called, it is guaranteed to be invoked before the first [`startRequest(_:)`](./startrequest%28_%29.md) call.

This method is synchronous. The prerolling won’t finish until the method returns.

## Parameters

- `renderHint`: Information about the upcoming composition requests.

## See Also

### Preparing to render frames
- [func anticipateRendering(using: AVVideoCompositionRenderHint)](./anticipaterendering%28using%29.md)
  Informs a custom video compositor about upcoming rendering requests.
- [class AVVideoCompositionRenderHint](../avvideocompositionrenderhint.md)
  Information about upcoming composition requests, such as composition start time and end time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositing/prerollforrendering(using:))*