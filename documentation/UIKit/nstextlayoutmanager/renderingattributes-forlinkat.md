# renderingAttributes(forLink:at:)

**Framework**: UIKit  
**Kind**: method

Returns a dictionary of rendering attributes for rendering a link.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func renderingAttributes(forLink link: Any, at location: any NSTextLocation) -> [NSAttributedString.Key : Any]
```

#### Return Value

A  dictionary of rendering attributes.

#### Discussion

As with other rendering attributes, specifying [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull) removes the attribute from the final attributes the framework uses for rendering. It has priority over the general rendering attributes.

## Parameters

- `link`: The link.
- `location`: The location of the link in the text.

## See Also

- [class var linkRenderingAttributes: [NSAttributedString.Key : Any]](nstextlayoutmanager/linkrenderingattributes.md)
  Returns the default set of attributes for rendering a link.
- [func addRenderingAttribute(NSAttributedString.Key, value: Any?, for: NSTextRange)](nstextlayoutmanager/addrenderingattribute(_:value:for:).md)
  Sets the rendering attribute for the value and range you specify.
- [func enumerateRenderingAttributes(from: any NSTextLocation, reverse: Bool, using: (NSTextLayoutManager, [NSAttributedString.Key : Any], NSTextRange) -> Bool)](nstextlayoutmanager/enumeraterenderingattributes(from:reverse:using:).md)
  Enumerates the rendering attributes from a location you specify.
- [func invalidateRenderingAttributes(for: NSTextRange)](nstextlayoutmanager/invalidaterenderingattributes(for:).md)
  Invalidates the rendering attributes of the specified text range.
- [func removeRenderingAttribute(NSAttributedString.Key, for: NSTextRange)](nstextlayoutmanager/removerenderingattribute(_:for:).md)
  Removes the rendering attribute from the specified text range.
- [func setRenderingAttributes([NSAttributedString.Key : Any], for: NSTextRange)](nstextlayoutmanager/setrenderingattributes(_:for:).md)
  Sets the rendering attributes for the range you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/renderingattributes(forlink:at:))*