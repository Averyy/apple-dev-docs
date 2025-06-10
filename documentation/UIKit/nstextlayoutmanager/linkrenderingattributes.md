# linkRenderingAttributes

**Framework**: UIKit  
**Kind**: property

Returns the default set of attributes for rendering a link.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class var linkRenderingAttributes: [NSAttributedString.Key : Any] { get }
```

#### Discussion

The base [`NSTextLayoutManager`](nstextlayoutmanager.md) class returns with [`single`](nsunderlinestyle/single.md) for [`underlineStyle`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key/underlineStyle) in Swift or [`NSUnderlineStyleAttributeName`](nsunderlinestyleattributename.md) in Objective-C, and the platform link color for [`foregroundColor`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key/foregroundColor) in Swift or [`NSForegroundColorAttributeName`](nsforegroundcolorattributename.md) in Objective-C. The platform color for macOS is `linkColor`. Other platforms uses `blueColor`.

## See Also

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
- [func setRenderingAttributes([NSAttributedString.Key : Any], for: NSTextRange)](nstextlayoutmanager/setrenderingattributes(_:for:).md)
  Sets the rendering attributes for the range you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/linkrenderingattributes)*