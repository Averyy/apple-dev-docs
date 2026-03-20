# setCaptionPreviewProfileID(_:position:text:)

**Framework**: AVFoundation  
**Kind**: method

Starts displaying a caption preview with the specified accessibility profile.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```swift
func setCaptionPreviewProfileID(_ profileID: String, position: CGPoint, text: String?)
```

#### Discussion

This method enables a preview mode that displays sample caption text using the visual appearance settings from the specified accessibility profile. The preview replaces any currently active subtitles and/or closed captions while active. The sample caption text position can be specified to avoid UI controls.

> **Note**: You must call [`stopShowingCaptionPreview()`](avplayerlayer/stopshowingcaptionpreview().md) to exit the preview.

## Parameters

- `profileID`: The identifier of the accessibility profile to use for caption appearance. Profile IDs can be obtained from `MACaptionAppearanceCopyProfileIDs()`. This determines font, color, background, and other visual characteristics.
- `position`: A CGPoint that defines the position (in points) of the caption preview relative to the default positioning of content captions (centered near the bottom of the video). Position values can be negative. (0, 0) represents the default positioning.
- `text`: Optional custom text to display in the preview. If `nil`, a standard localized preview message will be shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlayer/setcaptionpreviewprofileid(_:position:text:))*