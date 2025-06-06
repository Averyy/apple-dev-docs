# renderContextChanged(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Tells the compositor that the composition changed render contexts.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func renderContextChanged(_ newRenderContext: AVVideoCompositionRenderContext)
```

## Parameters

- `newRenderContext`: The new render context of the video composition.

## See Also

- [class AVVideoCompositionRenderContext](avvideocompositionrendercontext.md)
  An object that defines the context in which custom compositors render pixel buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositing/rendercontextchanged(_:))*