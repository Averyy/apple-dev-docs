# quickLookPreviewableItems(inRanges:)

**Framework**: AppKit  
**Kind**: method

Returns an array of URLs for items that can be displayed by QuickLook in the specified ranges.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func quickLookPreviewableItems(inRanges ranges: [NSValue]) -> [any QLPreviewItem]
```

#### Return Value

Returns an array of document URLs for text attachment content, if available.

#### Discussion

Each preview item must conform to the [`QLPreviewItem`](https://developer.apple.com/documentation/QuickLookUI/QLPreviewItem) protocol.

## Parameters

- `ranges`: An array of ranges.

## See Also

- [func updateQuickLookPreviewPanel()](nstextview/updatequicklookpreviewpanel.md)
  Notifies the QuickLook panel that an update may be required.
- [func toggleQuickLookPreviewPanel(Any?)](nstextview/togglequicklookpreviewpanel(_:).md)
  An action message that toggles the visibility state of the Quick Look preview panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/quicklookpreviewableitems(inranges:))*