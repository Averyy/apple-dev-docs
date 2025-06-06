# previewPanel(_:transitionImageFor:contentRect:)

**Framework**: Quick Look UI  
**Kind**: method

Returns the image to use for the transition zoom effect for a given item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func previewPanel(_ panel: QLPreviewPanel!, transitionImageFor item: (any QLPreviewItem)!, contentRect: UnsafeMutablePointer<NSRect>!) -> Any!
```

#### Return Value

The image to use for the transition zoom effect for the `item`.

#### Discussion

The system invokes this optional method when the preview panel opens or closes to provide a smooth transition when zooming. The return type of the function should be an instance of [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage).

## Parameters

- `panel`: The preview panel.
- `item`: The item the system is previewing.
- `contentRect`: The rectangle within a preview image that actually represents the content of the document. For icons, the actual rectangle is typically smaller than the icon itself.

## See Also

- [func previewPanel(QLPreviewPanel!, handle: NSEvent!) -> Bool](qlpreviewpaneldelegate/previewpanel(_:handle:).md)
  Handles an event that the preview panel receives, but doesn’t handle.
- [func previewPanel(QLPreviewPanel!, sourceFrameOnScreenFor: (any QLPreviewItem)!) -> NSRect](qlpreviewpaneldelegate/previewpanel(_:sourceframeonscreenfor:).md)
  Returns the screen rectangle for a given preview item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldelegate/previewpanel(_:transitionimagefor:contentrect:))*