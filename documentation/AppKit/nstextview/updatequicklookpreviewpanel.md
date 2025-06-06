# updateQuickLookPreviewPanel()

**Framework**: AppKit  
**Kind**: method

Notifies the QuickLook panel that an update may be required.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func updateQuickLookPreviewPanel()
```

#### Discussion

Notifies the  [`QLPreviewPanel`](https://developer.apple.com/documentation/QuickLookUI/QLPreviewPanel) class for possible status changes with the data source or controller.  Typically invoked in response to selection changes.

## See Also

- [func toggleQuickLookPreviewPanel(Any?)](nstextview/togglequicklookpreviewpanel(_:).md)
  An action message that toggles the visibility state of the Quick Look preview panel.
- [func quickLookPreviewableItems(inRanges: [NSValue]) -> [any QLPreviewItem]](nstextview/quicklookpreviewableitems(inranges:).md)
  Returns an array of URLs for items that can be displayed by QuickLook in the specified ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/updatequicklookpreviewpanel())*