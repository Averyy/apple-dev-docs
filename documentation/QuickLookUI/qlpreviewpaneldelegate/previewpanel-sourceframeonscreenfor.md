# previewPanel(_:sourceFrameOnScreenFor:)

**Framework**: Quick Look UI  
**Kind**: method

Returns the screen rectangle for a given preview item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func previewPanel(_ panel: QLPreviewPanel!, sourceFrameOnScreenFor item: (any QLPreviewItem)!) -> NSRect
```

#### Return Value

The screen rectangle for the given preview item. Return [`NSZeroRect`](https://developer.apple.com/documentation/Foundation/NSZeroRect) if there is no origin point (this will produce a fade of the panel).

#### Discussion

The system invokes this optional method when the preview panel opens or closes to provide a zoom effect. You should return — in screen coordinates — the rectangle that displays the specified preview item.

## Parameters

- `panel`: The preview panel.
- `item`: The preview item for which the screen rectangle is required.

## See Also

- [func previewPanel(QLPreviewPanel!, handle: NSEvent!) -> Bool](qlpreviewpaneldelegate/previewpanel(_:handle:).md)
  Handles an event that the preview panel receives, but doesn’t handle.
- [func previewPanel(QLPreviewPanel!, transitionImageFor: (any QLPreviewItem)!, contentRect: UnsafeMutablePointer<NSRect>!) -> Any!](qlpreviewpaneldelegate/previewpanel(_:transitionimagefor:contentrect:).md)
  Returns the image to use for the transition zoom effect for a given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldelegate/previewpanel(_:sourceframeonscreenfor:))*