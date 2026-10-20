# invalidateRenderingAttributes(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invalidates the rendering attributes of the specified text range.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func invalidateRenderingAttributes(for textRange: NSTextRange)
```

```objc
- (void) invalidateRenderingAttributesForTextRange:(NSTextRange *) textRange;
```

## Parameters

- `textRange`: The range of the text to invalidate.

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
- [func removeRenderingAttribute(NSAttributedString.Key, for: NSTextRange)](./removerenderingattribute%28_,for%29.md)
  Removes the rendering attribute from the specified text range.
- [func setRenderingAttributes([NSAttributedString.Key : Any], for: NSTextRange)](./setrenderingattributes%28_,for%29.md)
  Sets the rendering attributes for the range you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/invalidaterenderingattributes(for:))*