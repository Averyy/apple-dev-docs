# allowsVideoFrameAnalysis

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether to perform video frame analysis.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
var allowsVideoFrameAnalysis: Bool { get set }
```

#### Discussion

If the value is `true`, a player view tries to find objects, text, and people when you pause media playback. If it finds an object, the user is able to interact with it using a long press to present a context menu.

The default value is `true`.

## See Also

- [var videoFrameAnalysisTypes: AVVideoFrameAnalysisType](avplayerview/videoframeanalysistypes.md)
- [struct AVVideoFrameAnalysisType](avvideoframeanalysistype.md)
  Constants that define the types of analysis a player view controller may perform on a paused video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/allowsvideoframeanalysis)*