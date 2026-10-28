# toggleQuickLookPreviewPanel(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

An action message that toggles the visibility state of the Quick Look preview panel.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBAction
func toggleQuickLookPreviewPanel(_ sender: Any?)
```

```objc
- (void) toggleQuickLookPreviewPanel:(id) sender;
```

## Discussion

This action message toggles the visibility state of the Quick Look preview panel if the receiver is the current Quick Look controller.

## Parameters

- `sender`: The message sender.

## See Also

### Supporting QuickLook
- [func updateQuickLookPreviewPanel()](./updatequicklookpreviewpanel%28%29.md)
  Notifies the QuickLook panel that an update may be required.
- [func quickLookPreviewableItems(inRanges: [NSValue]) -> [any QLPreviewItem]](./quicklookpreviewableitems%28inranges%29.md)
  Returns an array of URLs for items that can be displayed by QuickLook in the specified ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/togglequicklookpreviewpanel(_:))*