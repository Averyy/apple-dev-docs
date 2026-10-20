# updateQuickLookPreviewPanel()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the QuickLook panel that an update may be required.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func updateQuickLookPreviewPanel()
```

```objc
- (void) updateQuickLookPreviewPanel;
```

#### Discussion

Notifies the  [`QLPreviewPanel`](../../QuickLookUI/qlpreviewpanel.md) class for possible status changes with the data source or controller.  Typically invoked in response to selection changes.

## See Also

### Supporting QuickLook
- [func toggleQuickLookPreviewPanel(Any?)](./togglequicklookpreviewpanel%28_%29.md)
  An action message that toggles the visibility state of the Quick Look preview panel.
- [func quickLookPreviewableItems(inRanges: [NSValue]) -> [any QLPreviewItem]](./quicklookpreviewableitems%28inranges%29.md)
  Returns an array of URLs for items that can be displayed by QuickLook in the specified ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/updatequicklookpreviewpanel())*