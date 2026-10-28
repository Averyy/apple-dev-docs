# renderingAttributes(forLink:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSDictionary<NSString *,id> *) renderingAttributesForLink:(id) link atLocation:(id<NSTextLocation>) location;
```

## Return Value

A  dictionary of rendering attributes.

## Discussion

As with other rendering attributes, specifying [`NSNull`](../../Foundation/nsnull.md) removes the attribute from the final attributes the framework uses for rendering. It has priority over the general rendering attributes.

## Parameters

- `link`: The link.
- `location`: The location of the link in the text.

## See Also

### Adjusting rendering
- [class var linkRenderingAttributes: [NSAttributedString.Key : Any]](./linkrenderingattributes.md)
  Returns the default set of attributes for rendering a link.
- [func addRenderingAttribute(NSAttributedString.Key, value: Any?, for: NSTextRange)](./addrenderingattribute%28_,value,for%29.md)
  Sets the rendering attribute for the value and range you specify.
- [func enumerateRenderingAttributes(from: any NSTextLocation, reverse: Bool, using: (NSTextLayoutManager, [NSAttributedString.Key : Any], NSTextRange) -> Bool)](./enumeraterenderingattributes%28from,reverse,using%29.md)
  Enumerates the rendering attributes from a location you specify.
- [func invalidateRenderingAttributes(for: NSTextRange)](./invalidaterenderingattributes%28for%29.md)
  Invalidates the rendering attributes of the specified text range.
- [func removeRenderingAttribute(NSAttributedString.Key, for: NSTextRange)](./removerenderingattribute%28_,for%29.md)
  Removes the rendering attribute from the specified text range.
- [func setRenderingAttributes([NSAttributedString.Key : Any], for: NSTextRange)](./setrenderingattributes%28_,for%29.md)
  Sets the rendering attributes for the range you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/renderingattributes(forlink:at:))*