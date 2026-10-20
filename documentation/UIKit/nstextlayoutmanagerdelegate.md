# NSTextLayoutManagerDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

Optional methods that delegates implement to respond to layout changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSTextLayoutManagerDelegate : NSObjectProtocol
```

```objc
@protocol NSTextLayoutManagerDelegate <NSObject>
```

## Topics

### Responding to layout changes
- [func textLayoutManager(NSTextLayoutManager, renderingAttributesForLink: Any, at: any NSTextLocation, defaultAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]?](./nstextlayoutmanagerdelegate/textlayoutmanager%28_,renderingattributesforlink,at,defaultattributes%29.md)
  The method the framework calls to return a dictionary of attributes for rendering a link attribute name.
- [func textLayoutManager(NSTextLayoutManager, shouldBreakLineBefore: any NSTextLocation, hyphenating: Bool) -> Bool](./nstextlayoutmanagerdelegate/textlayoutmanager%28_,shouldbreaklinebefore,hyphenating%29.md)
  The method the framework calls to determine the soft line break point.
- [func textLayoutManager(NSTextLayoutManager, textLayoutFragmentFor: any NSTextLocation, in: NSTextElement) -> NSTextLayoutFragment](./nstextlayoutmanagerdelegate/textlayoutmanager%28_,textlayoutfragmentfor,in%29.md)
  The method the framework calls to give the delegate an opportunity to return a custom text layout fragment.
### Reusing text attachment view providers
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate)*