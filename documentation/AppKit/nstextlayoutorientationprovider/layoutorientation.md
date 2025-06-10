# layoutOrientation

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

The default layout orientation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var layoutOrientation: NSLayoutManager.TextLayoutOrientation { get }
```

#### Discussion

This property contains the default layout orientation for text in the object that adopts the protocol. If the text contains an explicit [`verticalGlyphForm`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key/verticalGlyphForm) attribute, that attribute overrides the value in this property. When rendering, TextKit assumes the coordinate system is appropriately rotated.

## See Also

- [NSLayoutManager.TextLayoutOrientation](nslayoutmanager/textlayoutorientation.md)
  Constants that describe the text layout orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutorientationprovider/layoutorientation)*