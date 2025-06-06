# addRenderingAttribute(_:value:for:)

**Framework**: AppKit  
**Kind**: method

Sets the rendering attribute for the value and range you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func addRenderingAttribute(_ renderingAttribute: NSAttributedString.Key, value: Any?, for textRange: NSTextRange)
```

#### Discussion

Passing `nil` overrides the specified attribute by removing it from the final attributes the framework passes to the layout and rendering engine. This is a convenience method for [`setRenderingAttributes(_:for:)`](nstextlayoutmanager/setrenderingattributes(_:for:).md).

## Parameters

- `renderingAttribute`: The   that represents the attribute.
- `value`: The value for the attribute.
- `textRange`: The range over which to apply the attribute.

## See Also

- [class var linkRenderingAttributes: [NSAttributedString.Key : Any]](nstextlayoutmanager/linkrenderingattributes.md)
  Returns the default set of attributes for rendering a link.
- [func enumerateRenderingAttributes(from: any NSTextLocation, reverse: Bool, using: (NSTextLayoutManager, [NSAttributedString.Key : Any], NSTextRange) -> Bool)](nstextlayoutmanager/enumeraterenderingattributes(from:reverse:using:).md)
  Enumerates the rendering attributes from a location you specify.
- [func renderingAttributes(forLink: Any, at: any NSTextLocation) -> [NSAttributedString.Key : Any]](nstextlayoutmanager/renderingattributes(forlink:at:).md)
  Returns a dictionary of rendering attributes for rendering a link.
- [func invalidateRenderingAttributes(for: NSTextRange)](nstextlayoutmanager/invalidaterenderingattributes(for:).md)
  Invalidates the rendering attributes of the specified text range.
- [func removeRenderingAttribute(NSAttributedString.Key, for: NSTextRange)](nstextlayoutmanager/removerenderingattribute(_:for:).md)
  Removes the rendering attribute from the specified text range.
- [func setRenderingAttributes([NSAttributedString.Key : Any], for: NSTextRange)](nstextlayoutmanager/setrenderingattributes(_:for:).md)
  Sets the rendering attributes for the range you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/addrenderingattribute(_:value:for:))*