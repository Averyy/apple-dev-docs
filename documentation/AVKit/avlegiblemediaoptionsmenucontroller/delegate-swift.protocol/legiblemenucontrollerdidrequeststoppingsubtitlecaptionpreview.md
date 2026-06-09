# legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview(_:)

**Framework**: AVKit  
**Kind**: method

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

#### Discussion

Called when the caption preview should be hidden

The client should hide any active caption preview.

## Parameters

- `menuController`: The legible options menu controller.

## See Also

- [func legibleMenuController(AVLegibleMediaOptionsMenuController, didChange: AVLegibleMediaOptionsMenuState)](avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didchange:).md)
- [func legibleMenuController(AVLegibleMediaOptionsMenuController, didRequestCaptionPreviewForProfileID: String)](avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didrequestcaptionpreviewforprofileid:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview(_:))*