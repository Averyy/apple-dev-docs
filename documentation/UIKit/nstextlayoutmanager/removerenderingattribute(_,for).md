# removeRenderingAttribute(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes the rendering attribute from the specified text range.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func removeRenderingAttribute(_ renderingAttribute: NSAttributedString.Key, for textRange: NSTextRange)
```

```objc
- (void) removeRenderingAttribute:(NSAttributedStringKey) renderingAttribute forTextRange:(NSTextRange *) textRange;
```

## Parameters

- `renderingAttribute`: The [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md) attribute to remove
- `textRange`: The range over which to remove the rendering attribute.

## See Also

### Adjusting rendering
- [class var linkRenderingAttributes: [NSAttributedString.Key : Any]](./linkrenderingattributes.md)
  Returns the default set of attributes for rendering a link.
- [func addRenderingAttribute(NSAttributedString.Key, value: Any?, for: NSTextRange)](./addrenderingattribute%28_,value,for%29.md)
  Sets the rendering attribute for the value and range you specify.
- [func enumerateRenderingAttributes(from: any NSTextLocation, reverse: Bool, using: (NSTextLayoutManager, [NSAttributedString.Key : Any], NSTextRange) -> Bool)](./enumeraterenderingattributes%28from,reverse,using%29.md)
  Enumerates the rendering attributes from a location you specify.
- [func renderingAttributes(forLink: Any, at: any NSTextLocation) -> [NSAttributedString.Key : Any]](./renderingattributes%28forlink,at%29.md)
  Returns a dictionary of rendering attributes for rendering a link.
- [func invalidateRenderingAttributes(for: NSTextRange)](./invalidaterenderingattributes%28for%29.md)
  Invalidates the rendering attributes of the specified text range.
- [func setRenderingAttributes([NSAttributedString.Key : Any], for: NSTextRange)](./setrenderingattributes%28_,for%29.md)
  Sets the rendering attributes for the range you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/removerenderingattribute(_:for:))*