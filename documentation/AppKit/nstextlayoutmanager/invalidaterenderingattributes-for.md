# invalidateRenderingAttributes(for:)

**Framework**: AppKit  
**Kind**: method

Invalidates the rendering attributes of the specified text range.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func invalidateRenderingAttributes(for textRange: NSTextRange)
```

## Parameters

- `textRange`: The range of the text to invalidate.

## See Also

- [class var linkRenderingAttributes: [NSAttributedString.Key : Any]](nstextlayoutmanager/linkrenderingattributes.md)
  Returns the default set of attributes for rendering a link.
- [func addRenderingAttribute(NSAttributedString.Key, value: Any?, for: NSTextRange)](nstextlayoutmanager/addrenderingattribute(_:value:for:).md)
  Sets the rendering attribute for the value and range you specify.
- [func enumerateRenderingAttributes(from: any NSTextLocation, reverse: Bool, using: (NSTextLayoutManager, [NSAttributedString.Key : Any], NSTextRange) -> Bool)](nstextlayoutmanager/enumeraterenderingattributes(from:reverse:using:).md)
  Enumerates the rendering attributes from a location you specify.
- [func renderingAttributes(forLink: Any, at: any NSTextLocation) -> [NSAttributedString.Key : Any]](nstextlayoutmanager/renderingattributes(forlink:at:).md)
  Returns a dictionary of rendering attributes for rendering a link.
- [func removeRenderingAttribute(NSAttributedString.Key, for: NSTextRange)](nstextlayoutmanager/removerenderingattribute(_:for:).md)
  Removes the rendering attribute from the specified text range.
- [func setRenderingAttributes([NSAttributedString.Key : Any], for: NSTextRange)](nstextlayoutmanager/setrenderingattributes(_:for:).md)
  Sets the rendering attributes for the range you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/invalidaterenderingattributes(for:))*