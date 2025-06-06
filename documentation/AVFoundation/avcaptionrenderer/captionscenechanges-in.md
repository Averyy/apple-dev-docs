# captionSceneChanges(in:)

**Framework**: AVFoundation  
**Kind**: method

Determine render time ranges within an enclosing time range to account for visual changes among captions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func captionSceneChanges(in consideredTimeRange: CMTimeRange) -> [AVCaptionRenderer.Scene]
```

#### Return Value

An array of render scenes for the time range, or an empty array if there are none.

## Parameters

- `consideredTimeRange`: The time range to consider for rendering.

## See Also

- [AVCaptionRenderer.Scene](avcaptionrenderer/scene.md)
  An object that holds a time range and an associated state which indicates when the renderer draws output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/captionscenechanges(in:))*