# captionPreview(forProfileID:extendedLanguageTag:renderSize:)

**Framework**: AVFoundation  
**Kind**: method

Generate a caption preview attributed string for the specified profile ID.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```swift
class func captionPreview(forProfileID profileID: String, extendedLanguageTag: String?, renderSize: CGSize) -> NSAttributedString
```

#### Return Value

An NSAttributedString containing the caption preview.

#### Discussion

Returns an attributed string containing a preview of captions rendered using the specified profile ID.

> ❗ **Important**: It is strongly recommended that the caller take appropriate measures to prevent blocking essential services such as the user interface, for example, by avoiding calling this method in the main thread.

## Parameters

- `profileID`: The identifier of the accessibility profile to use for caption appearance. Profile IDs can be obtained from MACaptionAppearanceCopyProfileIDs(). This determines font, color, background, and other visual characteristics.
- `extendedLanguageTag`: The IETF BCP 47 (RFC 4646) language identifier that will be used to generate the localized caption preview text. If nil, the system language will be used.
- `renderSize`: The size of the layer into which the captions will be rendered. This determines the layout and positioning of the caption text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/captionpreview(forprofileid:extendedlanguagetag:rendersize:))*