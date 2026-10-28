# legibleMenuController(_:didRequestCaptionPreviewForProfileID:)

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
optional func legibleMenuController(_ menuController: AVLegibleMediaOptionsMenuController, didRequestCaptionPreviewForProfileID profileID: String)
```

```objc
- (void) legibleMenuController:(AVLegibleMediaOptionsMenuController *) menuController didRequestCaptionPreviewForProfileID:(NSString *) profileID;
```

## Discussion

Called when a caption preview should be displayed

The client should display a caption preview using the MACaptionAppearance profile ID provided. The client is responsible for rendering and positioning the preview.

## Parameters

- `menuController`: The legible options menu controller.
- `profileID`: MACaptionAppearance profile ID as an NSString for the caption style to preview

## See Also

### Responding to menu changes
- [func legibleMenuController(AVLegibleMediaOptionsMenuController, didChange: AVLegibleMediaOptionsMenuState)](./legiblemenucontroller%28_,didchange%29.md)
- [func legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview(AVLegibleMediaOptionsMenuController)](./legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didrequestcaptionpreviewforprofileid:))*