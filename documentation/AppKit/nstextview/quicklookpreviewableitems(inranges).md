# quickLookPreviewableItems(inRanges:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of URLs for items that can be displayed by QuickLook in the specified ranges.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func quickLookPreviewableItems(inRanges ranges: [NSValue]) -> [any QLPreviewItem]
```

```objc
- (NSArray<id<QLPreviewItem>> *) quickLookPreviewableItemsInRanges:(NSArray<NSValue *> *) ranges;
```

## Return Value

Returns an array of document URLs for text attachment content, if available.

## Discussion

Each preview item must conform to the [`QLPreviewItem`](../../QuickLookUI/qlpreviewitem.md) protocol.

## Parameters

- `ranges`: An array of ranges.

## See Also

### Supporting QuickLook
- [func updateQuickLookPreviewPanel()](./updatequicklookpreviewpanel%28%29.md)
  Notifies the QuickLook panel that an update may be required.
- [func toggleQuickLookPreviewPanel(Any?)](./togglequicklookpreviewpanel%28_%29.md)
  An action message that toggles the visibility state of the Quick Look preview panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/quicklookpreviewableitems(inranges:))*