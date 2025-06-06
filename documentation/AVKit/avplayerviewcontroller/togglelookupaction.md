# toggleLookupAction

**Framework**: AVKit  
**Kind**: property

An action that enables the visual lookup interface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
var toggleLookupAction: UIAction { get }
```

#### Discussion

When a user toggles the lookup UI, the state property is [`UIMenuElement.State.on`](https://developer.apple.com/documentation/UIKit/UIMenuElement/State/on), and is [`UIMenuElement.State.off`](https://developer.apple.com/documentation/UIKit/UIMenuElement/State/off) otherwise. The system disables the action’s attributes when there isn’t visual lookup data available or when the media is playing.

## See Also

- [var allowsVideoFrameAnalysis: Bool](avplayerviewcontroller/allowsvideoframeanalysis.md)
  A Boolean value that indicates whether to perform video frame analysis.
- [var videoFrameAnalysisTypes: AVVideoFrameAnalysisType](avplayerviewcontroller/videoframeanalysistypes.md)
  The types of analysis a player view controller performs on a paused video frame.
- [struct AVVideoFrameAnalysisType](avvideoframeanalysistype.md)
  Constants that define the types of analysis a player view controller may perform on a paused video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/togglelookupaction)*