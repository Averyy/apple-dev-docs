# legibleMenuController(_:didChange:)

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
optional func legibleMenuController(_ menuController: AVLegibleMediaOptionsMenuController, didChange state: AVLegibleMediaOptionsMenuState)
```

#### Discussion

Tells the delegate, when legible media options menu state changes.

## Parameters

- `menuController`: The legible options menu controller.
- `state`: The new menu state.

## See Also

- [func legibleMenuController(AVLegibleMediaOptionsMenuController, didRequestCaptionPreviewForProfileID: String)](avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didrequestcaptionpreviewforprofileid:).md)
- [func legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview(AVLegibleMediaOptionsMenuController)](avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didchange:))*