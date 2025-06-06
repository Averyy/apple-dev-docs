# setRenderingAttributes(_:for:)

**Framework**: AppKit  
**Kind**: method

Sets the rendering attributes for the range you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func setRenderingAttributes(_ renderingAttributes: [NSAttributedString.Key : Any], for textRange: NSTextRange)
```

## Parameters

- `renderingAttributes`: A dictionary of rendering attributes.
- `textRange`: The text range over which to apply  .

## See Also

- [class var linkRenderingAttributes: [NSAttributedString.Key : Any]](nstextlayoutmanager/linkrenderingattributes.md)
  Returns the default set of attributes for rendering a link.
- [func addRenderingAttribute(NSAttributedString.Key, value: Any?, for: NSTextRange)](nstextlayoutmanager/addrenderingattribute(_:value:for:).md)
  Sets the rendering attribute for the value and range you specify.
- [func enumerateRenderingAttributes(from: any NSTextLocation, reverse: Bool, using: (NSTextLayoutManager, [NSAttributedString.Key : Any], NSTextRange) -> Bool)](nstextlayoutmanager/enumeraterenderingattributes(from:reverse:using:).md)
  Enumerates the rendering attributes from a location you specify.
- [func renderingAttributes(forLink: Any, at: any NSTextLocation) -> [NSAttributedString.Key : Any]](nstextlayoutmanager/renderingattributes(forlink:at:).md)
  Returns a dictionary of rendering attributes for rendering a link.
- [func invalidateRenderingAttributes(for: NSTextRange)](nstextlayoutmanager/invalidaterenderingattributes(for:).md)
  Invalidates the rendering attributes of the specified text range.
- [func removeRenderingAttribute(NSAttributedString.Key, for: NSTextRange)](nstextlayoutmanager/removerenderingattribute(_:for:).md)
  Removes the rendering attribute from the specified text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/setrenderingattributes(_:for:))*