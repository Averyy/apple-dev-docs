# addRenderingAttribute(_:value:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the rendering attribute for the value and range you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func addRenderingAttribute(_ renderingAttribute: NSAttributedString.Key, value: Any?, for textRange: NSTextRange)
```

```objc
- (void) addRenderingAttribute:(NSAttributedStringKey) renderingAttribute value:(id) value forTextRange:(NSTextRange *) textRange;
```

#### Discussion

Passing `nil` overrides the specified attribute by removing it from the final attributes the framework passes to the layout and rendering engine. This is a convenience method for [`setRenderingAttributes(_:for:)`](./setrenderingattributes%28_,for%29.md).

## Parameters

- `renderingAttribute`: The [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md) that represents the attribute.
- `value`: The value for the attribute.
- `textRange`: The range over which to apply the attribute.

## See Also

### Adjusting rendering
- [class var linkRenderingAttributes: [NSAttributedString.Key : Any]](./linkrenderingattributes.md)
  Returns the default set of attributes for rendering a link.
- [func enumerateRenderingAttributes(from: any NSTextLocation, reverse: Bool, using: (NSTextLayoutManager, [NSAttributedString.Key : Any], NSTextRange) -> Bool)](./enumeraterenderingattributes%28from,reverse,using%29.md)
  Enumerates the rendering attributes from a location you specify.
- [func renderingAttributes(forLink: Any, at: any NSTextLocation) -> [NSAttributedString.Key : Any]](./renderingattributes%28forlink,at%29.md)
  Returns a dictionary of rendering attributes for rendering a link.
- [func invalidateRenderingAttributes(for: NSTextRange)](./invalidaterenderingattributes%28for%29.md)
  Invalidates the rendering attributes of the specified text range.
- [func removeRenderingAttribute(NSAttributedString.Key, for: NSTextRange)](./removerenderingattribute%28_,for%29.md)
  Removes the rendering attribute from the specified text range.
- [func setRenderingAttributes([NSAttributedString.Key : Any], for: NSTextRange)](./setrenderingattributes%28_,for%29.md)
  Sets the rendering attributes for the range you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/addrenderingattribute(_:value:for:))*