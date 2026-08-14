# NSTextLayoutManagerDelegate

**Framework**: AppKit  
**Kind**: protocol

Optional methods that delegates implement to respond to layout changes.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol NSTextLayoutManagerDelegate : NSObjectProtocol
```

#### Overview

Optional methods that delegates implement to respond to layout changes.

## Topics

### Responding to layout changes
- [func textLayoutManager(NSTextLayoutManager, renderingAttributesForLink: Any, at: any NSTextLocation, defaultAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]?](nstextlayoutmanagerdelegate/textlayoutmanager(_:renderingattributesforlink:at:defaultattributes:).md)
  Returns a dictionary of rendering attributes for rendering a link.
- [func textLayoutManager(NSTextLayoutManager, shouldBreakLineBefore: any NSTextLocation, hyphenating: Bool) -> Bool](nstextlayoutmanagerdelegate/textlayoutmanager(_:shouldbreaklinebefore:hyphenating:).md)
  Invoked while determining the soft line break point.
- [func textLayoutManager(NSTextLayoutManager, textLayoutFragmentFor: any NSTextLocation, in: NSTextElement) -> NSTextLayoutFragment](nstextlayoutmanagerdelegate/textlayoutmanager(_:textlayoutfragmentfor:in:).md)
  Returns a text layout fragment for the specified location in the text element.
### Instance Methods
- [func textLayoutManager(NSTextLayoutManager, cacheTextAttachmentViewProvider: NSTextAttachmentViewProvider, for: NSTextAttachment)](nstextlayoutmanagerdelegate/textlayoutmanager(_:cachetextattachmentviewprovider:for:).md)
  Notifies the delegate that a view provider associated with a text attachment is about to be invalidated.
- [func textLayoutManager(NSTextLayoutManager, retrieveCachedTextAttachmentViewProviderFor: NSTextAttachment) -> NSTextAttachmentViewProvider?](nstextlayoutmanagerdelegate/textlayoutmanager(_:retrievecachedtextattachmentviewproviderfor:).md)
  Returns a cached `NSTextAttachmentViewProvider` to be associated with a particular attachment.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [var delegate: (any NSTextLayoutManagerDelegate)?](nstextlayoutmanager/delegate.md)
  The delegate for the text layout manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanagerdelegate)*