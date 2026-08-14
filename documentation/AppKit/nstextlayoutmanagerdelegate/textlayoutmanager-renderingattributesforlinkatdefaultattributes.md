# textLayoutManager(_:renderingAttributesForLink:at:defaultAttributes:)

**Framework**: AppKit  
**Kind**: method

Returns a dictionary of rendering attributes for rendering a link.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, renderingAttributesForLink link: Any, at location: any NSTextLocation, defaultAttributes renderingAttributes: [NSAttributedString.Key : Any] = [:]) -> [NSAttributedString.Key : Any]?
```

#### Return Value

A dictionary of rendering attributes for the link, or `nil` to use defaults.

#### Discussion

Just as other rendering attributes, specifying [`NSNull`](https://developer.apple.com/documentation/foundation/nsnull) removes the attribute from the final attributes used for rendering. It has priority over the general rendering attributes.

The method the framework calls to return a dictionary of attributes for rendering a link attribute name.

## Parameters

- `textLayoutManager`: The text layout manager sending the message.
- `link`: The link object.
- `location`: The document location of the link.
- `renderingAttributes`: The default rendering attributes.

## See Also

- [func textLayoutManager(NSTextLayoutManager, shouldBreakLineBefore: any NSTextLocation, hyphenating: Bool) -> Bool](nstextlayoutmanagerdelegate/textlayoutmanager(_:shouldbreaklinebefore:hyphenating:).md)
  Invoked while determining the soft line break point.
- [func textLayoutManager(NSTextLayoutManager, textLayoutFragmentFor: any NSTextLocation, in: NSTextElement) -> NSTextLayoutFragment](nstextlayoutmanagerdelegate/textlayoutmanager(_:textlayoutfragmentfor:in:).md)
  Returns a text layout fragment for the specified location in the text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanagerdelegate/textlayoutmanager(_:renderingattributesforlink:at:defaultattributes:))*