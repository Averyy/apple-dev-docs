# textLayoutManager(_:textLayoutFragmentFor:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a text layout fragment for the specified location in the text element.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, textLayoutFragmentFor location: any NSTextLocation, in textElement: NSTextElement) -> NSTextLayoutFragment
```

```objc
- (NSTextLayoutFragment *) textLayoutManager:(NSTextLayoutManager *) textLayoutManager textLayoutFragmentForLocation:(id<NSTextLocation>) location inTextElement:(NSTextElement *) textElement;
```

## Return Value

A layout fragment for the location, or `nil` to use the default.

## Discussion

The delegate can provide an [`NSTextLayoutFragment`](../nstextlayoutfragment.md) specialized for an [`NSTextElement`](../nstextelement.md) subclass targeted for the rendering surface.

The method the framework calls to give the delegate an opportunity to return a custom text layout fragment.

## Discussion

Use this to provide an [`NSTextLayoutFragment`](../nstextlayoutfragment.md) specialized for an [`NSTextElement`](../nstextelement.md) subclass targeted for the rendering surface.

## Parameters

- `textLayoutManager`: The text layout manager sending the message.
- `location`: The document location.
- `textElement`: The text element containing the location.

## See Also

### Responding to layout changes
- [func textLayoutManager(NSTextLayoutManager, renderingAttributesForLink: Any, at: any NSTextLocation, defaultAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]?](./textlayoutmanager%28_,renderingattributesforlink,at,defaultattributes%29.md)
  Returns a dictionary of rendering attributes for rendering a link.
- [func textLayoutManager(NSTextLayoutManager, shouldBreakLineBefore: any NSTextLocation, hyphenating: Bool) -> Bool](./textlayoutmanager%28_,shouldbreaklinebefore,hyphenating%29.md)
  Invoked while determining the soft line break point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanagerdelegate/textlayoutmanager(_:textlayoutfragmentfor:in:))*