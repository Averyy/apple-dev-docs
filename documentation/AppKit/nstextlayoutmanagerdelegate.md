# NSTextLayoutManagerDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

Optional methods that delegates implement to respond to layout changes.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol NSTextLayoutManagerDelegate : NSObjectProtocol
```

```objc
@protocol NSTextLayoutManagerDelegate <NSObject>
```

#### Overview

Optional methods that delegates implement to respond to layout changes.

## Topics

### Responding to layout changes
- [func textLayoutManager(NSTextLayoutManager, renderingAttributesForLink: Any, at: any NSTextLocation, defaultAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]?](./nstextlayoutmanagerdelegate/textlayoutmanager%28_,renderingattributesforlink,at,defaultattributes%29.md)
  Returns a dictionary of rendering attributes for rendering a link.
- [func textLayoutManager(NSTextLayoutManager, shouldBreakLineBefore: any NSTextLocation, hyphenating: Bool) -> Bool](./nstextlayoutmanagerdelegate/textlayoutmanager%28_,shouldbreaklinebefore,hyphenating%29.md)
  Invoked while determining the soft line break point.
- [func textLayoutManager(NSTextLayoutManager, textLayoutFragmentFor: any NSTextLocation, in: NSTextElement) -> NSTextLayoutFragment](./nstextlayoutmanagerdelegate/textlayoutmanager%28_,textlayoutfragmentfor,in%29.md)
  Returns a text layout fragment for the specified location in the text element.
### Instance Methods
- [func textLayoutManager(NSTextLayoutManager, cacheTextAttachmentViewProvider: NSTextAttachmentViewProvider, for: NSTextAttachment)](./nstextlayoutmanagerdelegate/textlayoutmanager%28_,cachetextattachmentviewprovider,for%29.md)
  Notifies the delegate that a view provider associated with a text attachment is about to be invalidated.
- [func textLayoutManager(NSTextLayoutManager, retrieveCachedTextAttachmentViewProviderFor: NSTextAttachment) -> NSTextAttachmentViewProvider?](./nstextlayoutmanagerdelegate/textlayoutmanager%28_,retrievecachedtextattachmentviewproviderfor%29.md)
  Returns a cached `NSTextAttachmentViewProvider` to be associated with a particular attachment.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managing the layout process
- [var delegate: (any NSTextLayoutManagerDelegate)?](./nstextlayoutmanager/delegate.md)
  The delegate for the text layout manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanagerdelegate)*