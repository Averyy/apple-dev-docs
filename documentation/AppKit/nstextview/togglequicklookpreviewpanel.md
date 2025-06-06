# toggleQuickLookPreviewPanel(_:)

**Framework**: AppKit  
**Kind**: method

An action message that toggles the visibility state of the Quick Look preview panel.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBAction
@MainActor func toggleQuickLookPreviewPanel(_ sender: Any?)
```

#### Discussion

This action message toggles the visibility state of the Quick Look preview panel if the receiver is the current Quick Look controller.

## Parameters

- `sender`: The message sender.

## See Also

- [func updateQuickLookPreviewPanel()](nstextview/updatequicklookpreviewpanel.md)
  Notifies the QuickLook panel that an update may be required.
- [func quickLookPreviewableItems(inRanges: [NSValue]) -> [any QLPreviewItem]](nstextview/quicklookpreviewableitems(inranges:).md)
  Returns an array of URLs for items that can be displayed by QuickLook in the specified ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/togglequicklookpreviewpanel(_:))*