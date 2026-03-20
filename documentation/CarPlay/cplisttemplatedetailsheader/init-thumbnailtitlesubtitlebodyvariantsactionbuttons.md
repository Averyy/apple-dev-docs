# init(thumbnail:title:subtitle:bodyVariants:actionButtons:)

**Framework**: CarPlay  
**Kind**: init

Creates a new details header with the specified content and action buttons.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, bodyVariants: [NSAttributedString], actionButtons: [CPButton])
```

#### Return Value

A newly initialized CPListTemplateDetailsHeader instance.

#### Discussion

The thumbnail parameter is required and should not be nil. The title and subtitle are optional but at least one should be provided for meaningful content display. Action buttons will be displayed in the order provided in the array.

## Parameters

- `thumbnail`: The thumbnail image to display in the header. This image may include overlays, progress indicators, or other visual enhancements.
- `title`: The primary title text to display. Pass nil to hide the title.
- `subtitle`: The secondary subtitle text to display below the title. Pass nil to hide the subtitle.
- `bodyVariants`: The multiline metadata text to display below the subtitle. Pass nil to hide the metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/init(thumbnail:title:subtitle:bodyvariants:actionbuttons:))*