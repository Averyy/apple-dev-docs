# setRenderingAttributes(_:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the rendering attributes for the range you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func setRenderingAttributes(_ renderingAttributes: [NSAttributedString.Key : Any], for textRange: NSTextRange)
```

```objc
- (void) setRenderingAttributes:(NSDictionary<NSString *,id> *) renderingAttributes forTextRange:(NSTextRange *) textRange;
```

## Parameters

- `renderingAttributes`: A dictionary of rendering attributes.
- `textRange`: The text range over which to apply `renderingAttributes`.

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
- [func removeRenderingAttribute(NSAttributedString.Key, for: NSTextRange)](./removerenderingattribute%28_,for%29.md)
  Removes the rendering attribute from the specified text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/setrenderingattributes(_:for:))*