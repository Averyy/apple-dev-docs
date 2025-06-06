# textLayoutManager(_:textLayoutFragmentFor:in:)

**Framework**: UIKit  
**Kind**: method

The method the framework calls to give the delegate an opportunity to return a custom text layout fragment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, textLayoutFragmentFor location: any NSTextLocation, in textElement: NSTextElement) -> NSTextLayoutFragment
```

#### Return Value

An [`NSTextLayoutFragment`](nstextlayoutfragment.md).

#### Discussion

Use this to provide an [`NSTextLayoutFragment`](nstextlayoutfragment.md) specialized for an [`NSTextElement`](nstextelement.md) subclass targeted for the rendering surface.

## Parameters

- `textLayoutManager`: The text layout manager.
- `location`: The   of the link in the text element.
- `textElement`: The   that the method could return a custom   from.

## See Also

- [func textLayoutManager(NSTextLayoutManager, renderingAttributesForLink: Any, at: any NSTextLocation, defaultAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]?](nstextlayoutmanagerdelegate/textlayoutmanager(_:renderingattributesforlink:at:defaultattributes:).md)
  The method the framework calls to return a dictionary of attributes for rendering a link attribute name.
- [func textLayoutManager(NSTextLayoutManager, shouldBreakLineBefore: any NSTextLocation, hyphenating: Bool) -> Bool](nstextlayoutmanagerdelegate/textlayoutmanager(_:shouldbreaklinebefore:hyphenating:).md)
  The method the framework calls to determine the soft line break point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:textlayoutfragmentfor:in:))*