# legibleMenuController(_:didRequestCaptionPreviewForProfileID:)

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
optional func legibleMenuController(_ menuController: AVLegibleMediaOptionsMenuController, didRequestCaptionPreviewForProfileID profileID: String)
```

#### Discussion

Called when a caption preview should be displayed

The client should display a caption preview using the MACaptionAppearance profile ID provided. The client is responsible for rendering and positioning the preview.

## Parameters

- `menuController`: The legible options menu controller.
- `profileID`: MACaptionAppearance profile ID as an NSString for the caption style to preview

## See Also

- [func legibleMenuController(AVLegibleMediaOptionsMenuController, didChange: AVLegibleMediaOptionsMenuState)](avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didchange:).md)
- [func legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview(AVLegibleMediaOptionsMenuController)](avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didrequestcaptionpreviewforprofileid:))*