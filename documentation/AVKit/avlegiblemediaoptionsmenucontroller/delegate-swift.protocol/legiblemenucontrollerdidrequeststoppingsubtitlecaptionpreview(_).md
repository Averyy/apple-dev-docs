# legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview(_:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
optional func legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview(_ menuController: AVLegibleMediaOptionsMenuController)
```

```objc
- (void) legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview:(AVLegibleMediaOptionsMenuController *) menuController;
```

## Discussion

Called when the caption preview should be hidden

The client should hide any active caption preview.

## Parameters

- `menuController`: The legible options menu controller.

## See Also

### Responding to menu changes
- [func legibleMenuController(AVLegibleMediaOptionsMenuController, didChange: AVLegibleMediaOptionsMenuState)](./legiblemenucontroller%28_,didchange%29.md)
- [func legibleMenuController(AVLegibleMediaOptionsMenuController, didRequestCaptionPreviewForProfileID: String)](./legiblemenucontroller%28_,didrequestcaptionpreviewforprofileid%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview(_:))*