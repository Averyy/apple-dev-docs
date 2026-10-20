# AVLegibleMediaOptionsMenuController.Delegate

**Framework**: AVKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
protocol Delegate : NSObjectProtocol
```

```objc
@protocol AVLegibleMediaOptionsMenuControllerDelegate <NSObject>
```

#### Overview

Delegate protocol for AVLegibleMediaOptionsMenuController

Provides callbacks for caption preview display and enablement state changes.

## Topics

### Responding to menu changes
- [func legibleMenuController(AVLegibleMediaOptionsMenuController, didChange: AVLegibleMediaOptionsMenuState)](./delegate-swift.protocol/legiblemenucontroller%28_,didchange%29.md)
- [func legibleMenuController(AVLegibleMediaOptionsMenuController, didRequestCaptionPreviewForProfileID: String)](./delegate-swift.protocol/legiblemenucontroller%28_,didrequestcaptionpreviewforprofileid%29.md)
- [func legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview(AVLegibleMediaOptionsMenuController)](./delegate-swift.protocol/legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring a delegate
- [var delegate: (any AVLegibleMediaOptionsMenuController.Delegate)?](./delegate-swift.property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol)*