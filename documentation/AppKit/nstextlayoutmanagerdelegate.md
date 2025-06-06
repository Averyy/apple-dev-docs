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

## Topics

### Responding to layout changes
- [func textLayoutManager(NSTextLayoutManager, renderingAttributesForLink: Any, at: any NSTextLocation, defaultAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]?](nstextlayoutmanagerdelegate/textlayoutmanager(_:renderingattributesforlink:at:defaultattributes:).md)
  The method the framework calls to return a dictionary of attributes for rendering a link attribute name.
- [func textLayoutManager(NSTextLayoutManager, shouldBreakLineBefore: any NSTextLocation, hyphenating: Bool) -> Bool](nstextlayoutmanagerdelegate/textlayoutmanager(_:shouldbreaklinebefore:hyphenating:).md)
  The method the framework calls to determine the soft line break point.
- [func textLayoutManager(NSTextLayoutManager, textLayoutFragmentFor: any NSTextLocation, in: NSTextElement) -> NSTextLayoutFragment](nstextlayoutmanagerdelegate/textlayoutmanager(_:textlayoutfragmentfor:in:).md)
  The method the framework calls to give the delegate an opportunity to return a custom text layout fragment.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any NSTextLayoutManagerDelegate)?](nstextlayoutmanager/delegate.md)
  The delegate for the text layout manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanagerdelegate)*