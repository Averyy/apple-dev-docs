# textLayoutManager(_:renderingAttributesForLink:at:defaultAttributes:)

**Framework**: AppKit  
**Kind**: method

The method the framework calls to return a dictionary of attributes for rendering a link attribute name.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, renderingAttributesForLink link: Any, at location: any NSTextLocation, defaultAttributes renderingAttributes: [NSAttributedString.Key : Any] = [:]) -> [NSAttributedString.Key : Any]?
```

#### Return Value

A dictionary of attributes.

## Parameters

- `textLayoutManager`: The  .
- `link`: The link.
- `location`: The   of the link.
- `renderingAttributes`: A dictionary of attributes whose keys are   values.

## See Also

- [func textLayoutManager(NSTextLayoutManager, shouldBreakLineBefore: any NSTextLocation, hyphenating: Bool) -> Bool](nstextlayoutmanagerdelegate/textlayoutmanager(_:shouldbreaklinebefore:hyphenating:).md)
  The method the framework calls to determine the soft line break point.
- [func textLayoutManager(NSTextLayoutManager, textLayoutFragmentFor: any NSTextLocation, in: NSTextElement) -> NSTextLayoutFragment](nstextlayoutmanagerdelegate/textlayoutmanager(_:textlayoutfragmentfor:in:).md)
  The method the framework calls to give the delegate an opportunity to return a custom text layout fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanagerdelegate/textlayoutmanager(_:renderingattributesforlink:at:defaultattributes:))*