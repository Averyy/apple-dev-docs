# allowsVideoFrameAnalysis

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether to perform video frame analysis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
var allowsVideoFrameAnalysis: Bool { get set }
```

#### Discussion

If the value is [`true`](https://developer.apple.com/documentation/swift/true), a player view controller tries to find objects, text, and people when you pause media playback. If it finds an object, the user is able to interact with it using a long press to present a context menu.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var toggleLookupAction: UIAction](avplayerviewcontroller/togglelookupaction.md)
  An action that enables the visual lookup interface.
- [var videoFrameAnalysisTypes: AVVideoFrameAnalysisType](avplayerviewcontroller/videoframeanalysistypes.md)
  The types of analysis a player view controller performs on a paused video frame.
- [struct AVVideoFrameAnalysisType](avvideoframeanalysistype.md)
  Constants that define the types of analysis a player view controller may perform on a paused video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/allowsvideoframeanalysis)*