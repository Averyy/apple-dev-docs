# previewPanel(_:handle:)

**Framework**: Quick Look UI  
**Kind**: method  
**Role**: Instance Method

Handles an event that the preview panel receives, but doesn’t handle.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func previewPanel(_ panel: QLPreviewPanel!, handle event: NSEvent!) -> Bool
```

```objc
- (BOOL) previewPanel:(QLPreviewPanel *) panel handleEvent:(NSEvent *) event;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver handled the event; otherwise, [`false`](../../Swift/false.md).

## Discussion

The preview panel invokes this optional method when it receives an event it doesn’t handle.

## Parameters

- `panel`: The preview panel.
- `event`: The event that the preview panel wasn’t able to handle.

## See Also

### Optional Methods
- [func previewPanel(QLPreviewPanel!, sourceFrameOnScreenFor: (any QLPreviewItem)!) -> NSRect](./previewpanel%28_,sourceframeonscreenfor%29.md)
  Returns the screen rectangle for a given preview item.
- [func previewPanel(QLPreviewPanel!, transitionImageFor: (any QLPreviewItem)!, contentRect: UnsafeMutablePointer<NSRect>!) -> Any!](./previewpanel%28_,transitionimagefor,contentrect%29.md)
  Returns the image to use for the transition zoom effect for a given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldelegate/previewpanel(_:handle:))*