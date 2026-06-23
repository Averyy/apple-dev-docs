# textLayoutManager(_:shouldBreakLineBefore:hyphenating:)

**Framework**: AppKit  
**Kind**: method

Invoked while determining the soft line break point.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, shouldBreakLineBefore location: any NSTextLocation, hyphenating: Bool) -> Bool
```

#### Return Value

`true` to allow the break; `false` to prevent it.

#### Discussion

When `hyphenating` is `false`, [`NSTextLayoutManager`](nstextlayoutmanager.md) tries to find the next line break opportunity before location. When `hyphenating` is `true`, it is an auto-hyphenation point.

The method the framework calls to determine the soft line break point.

#### Discussion

When `hyphenating` is `false`, `NSTextLayoutManager` tries to find the next line break opportunity before location. When hyphenating is `true`, it’s an auto-hyphenation point.

## Parameters

- `textLayoutManager`: The text layout manager sending the message.
- `location`: The candidate break location.
- `hyphenating`: `true` if this is an auto-hyphenation point.

## See Also

- [func textLayoutManager(NSTextLayoutManager, renderingAttributesForLink: Any, at: any NSTextLocation, defaultAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]?](nstextlayoutmanagerdelegate/textlayoutmanager(_:renderingattributesforlink:at:defaultattributes:).md)
  Returns a dictionary of rendering attributes for rendering a link.
- [func textLayoutManager(NSTextLayoutManager, textLayoutFragmentFor: any NSTextLocation, in: NSTextElement) -> NSTextLayoutFragment](nstextlayoutmanagerdelegate/textlayoutmanager(_:textlayoutfragmentfor:in:).md)
  Returns a text layout fragment for the specified location in the text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanagerdelegate/textlayoutmanager(_:shouldbreaklinebefore:hyphenating:))*