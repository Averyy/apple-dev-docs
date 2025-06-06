# enumerateRenderingAttributes(from:reverse:using:)

**Framework**: UIKit  
**Kind**: method

Enumerates the rendering attributes from a location you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func enumerateRenderingAttributes(from location: any NSTextLocation, reverse: Bool, using block: (NSTextLayoutManager, [NSAttributedString.Key : Any], NSTextRange) -> Bool)
```

#### Discussion

This method only enumerates ranges with text that specify rendering attributes. Returning `false` from `block` breaks out of the enumeration.

## Parameters

- `location`: The location at which to start the enumeration.
- `reverse`: Whether to start the enumeration from the end of the range.
- `block`: A closure you provide to determine if the enumeration finishes early.

## See Also

- [class var linkRenderingAttributes: [NSAttributedString.Key : Any]](nstextlayoutmanager/linkrenderingattributes.md)
  Returns the default set of attributes for rendering a link.
- [func addRenderingAttribute(NSAttributedString.Key, value: Any?, for: NSTextRange)](nstextlayoutmanager/addrenderingattribute(_:value:for:).md)
  Sets the rendering attribute for the value and range you specify.
- [func renderingAttributes(forLink: Any, at: any NSTextLocation) -> [NSAttributedString.Key : Any]](nstextlayoutmanager/renderingattributes(forlink:at:).md)
  Returns a dictionary of rendering attributes for rendering a link.
- [func invalidateRenderingAttributes(for: NSTextRange)](nstextlayoutmanager/invalidaterenderingattributes(for:).md)
  Invalidates the rendering attributes of the specified text range.
- [func removeRenderingAttribute(NSAttributedString.Key, for: NSTextRange)](nstextlayoutmanager/removerenderingattribute(_:for:).md)
  Removes the rendering attribute from the specified text range.
- [func setRenderingAttributes([NSAttributedString.Key : Any], for: NSTextRange)](nstextlayoutmanager/setrenderingattributes(_:for:).md)
  Sets the rendering attributes for the range you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/enumeraterenderingattributes(from:reverse:using:))*