# textLayoutManager(_:renderingAttributesForLink:at:defaultAttributes:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary of rendering attributes for rendering a link.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, renderingAttributesForLink link: Any, at location: any NSTextLocation, defaultAttributes renderingAttributes: [NSAttributedString.Key : Any] = [:]) -> [NSAttributedString.Key : Any]?
```

```objc
- (NSDictionary<NSString *,id> *) textLayoutManager:(NSTextLayoutManager *) textLayoutManager renderingAttributesForLink:(id) link atLocation:(id<NSTextLocation>) location defaultAttributes:(NSDictionary<NSString *,id> *) renderingAttributes;
```

## Return Value

A dictionary of rendering attributes for the link, or `nil` to use defaults.

## Discussion

Just as other rendering attributes, specifying [`NSNull`](../../Foundation/nsnull.md) removes the attribute from the final attributes used for rendering. It has priority over the general rendering attributes.

The method the framework calls to return a dictionary of attributes for rendering a link attribute name.

## Parameters

- `textLayoutManager`: The text layout manager sending the message.
- `link`: The link object.
- `location`: The document location of the link.
- `renderingAttributes`: The default rendering attributes.

## See Also

### Responding to layout changes
- [func textLayoutManager(NSTextLayoutManager, shouldBreakLineBefore: any NSTextLocation, hyphenating: Bool) -> Bool](./textlayoutmanager%28_,shouldbreaklinebefore,hyphenating%29.md)
  Invoked while determining the soft line break point.
- [func textLayoutManager(NSTextLayoutManager, textLayoutFragmentFor: any NSTextLocation, in: NSTextElement) -> NSTextLayoutFragment](./textlayoutmanager%28_,textlayoutfragmentfor,in%29.md)
  Returns a text layout fragment for the specified location in the text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanagerdelegate/textlayoutmanager(_:renderingattributesforlink:at:defaultattributes:))*