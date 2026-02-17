# legibleMenuController(_:didRequestCaptionPreviewForProfileID:)

**Framework**: AVKit  
**Kind**: method

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didrequestcaptionpreviewforprofileid:))*