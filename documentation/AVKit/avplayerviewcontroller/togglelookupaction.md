# toggleLookupAction

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

An action that enables the visual lookup interface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+

## Declaration

```swift
var toggleLookupAction: UIAction { get }
```

```objc
@property (nonatomic, readonly) UIAction * toggleLookupAction;
```

#### Discussion

When a user toggles the lookup UI, the state property is [`UIMenuElement.State.on`](../../UIKit/uimenuelement/state/on.md), and is [`UIMenuElement.State.off`](../../UIKit/uimenuelement/state/off.md) otherwise. The system disables the action’s attributes when there isn’t visual lookup data available or when the media is playing.

## See Also

### Configuring frame analysis
- [var allowsVideoFrameAnalysis: Bool](./allowsvideoframeanalysis.md)
  A Boolean value that indicates whether to perform video frame analysis.
- [var videoFrameAnalysisTypes: AVVideoFrameAnalysisType](./videoframeanalysistypes.md)
  The types of analysis a player view controller performs on a paused video frame.
- [struct AVVideoFrameAnalysisType](../avvideoframeanalysistype.md)
  Constants that define the types of analysis a player view controller may perform on a paused video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/togglelookupaction)*