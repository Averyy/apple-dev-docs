# enumerateRenderingAttributes(from:reverse:using:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Enumerates the rendering attributes from a location you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func enumerateRenderingAttributes(from location: any NSTextLocation, reverse: Bool, using block: (NSTextLayoutManager, [NSAttributedString.Key : Any], NSTextRange) -> Bool)
```

```objc
- (void) enumerateRenderingAttributesFromLocation:(id<NSTextLocation>) location reverse:(BOOL) reverse usingBlock:(BOOL (^)(NSTextLayoutManager *textLayoutManager, NSDictionary<NSString *,id> *attributes, NSTextRange *textRange)) block;
```

#### Discussion

This method only enumerates ranges with text that specify rendering attributes. Returning `false` from `block` breaks out of the enumeration.

## Parameters

- `location`: The location at which to start the enumeration.
- `reverse`: Whether to start the enumeration from the end of the range.
- `block`: A closure you provide to determine if the enumeration finishes early.

## See Also

### Adjusting rendering
- [class var linkRenderingAttributes: [NSAttributedString.Key : Any]](./linkrenderingattributes.md)
  Returns the default set of attributes for rendering a link.
- [func addRenderingAttribute(NSAttributedString.Key, value: Any?, for: NSTextRange)](./addrenderingattribute%28_,value,for%29.md)
  Sets the rendering attribute for the value and range you specify.
- [func renderingAttributes(forLink: Any, at: any NSTextLocation) -> [NSAttributedString.Key : Any]](./renderingattributes%28forlink,at%29.md)
  Returns a dictionary of rendering attributes for rendering a link.
- [func invalidateRenderingAttributes(for: NSTextRange)](./invalidaterenderingattributes%28for%29.md)
  Invalidates the rendering attributes of the specified text range.
- [func removeRenderingAttribute(NSAttributedString.Key, for: NSTextRange)](./removerenderingattribute%28_,for%29.md)
  Removes the rendering attribute from the specified text range.
- [func setRenderingAttributes([NSAttributedString.Key : Any], for: NSTextRange)](./setrenderingattributes%28_,for%29.md)
  Sets the rendering attributes for the range you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/enumeraterenderingattributes(from:reverse:using:))*