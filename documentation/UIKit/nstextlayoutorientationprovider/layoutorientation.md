# layoutOrientation

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The default layout orientation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var layoutOrientation: NSLayoutManager.TextLayoutOrientation { get }
```

#### Discussion

This property contains the default layout orientation for text in the object that adopts the protocol. If the text contains an explicit [`verticalGlyphForm`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1528658-verticalglyphform) attribute in Swift or an [`NSVerticalGlyphFormAttributeName`](nsverticalglyphformattributename.md) attribute in Objective-C, that attribute overrides the value in this property. When rendering, TextKit assumes the coordinate system is appropriately rotated.

## See Also

- [NSLayoutManager.TextLayoutOrientation](nslayoutmanager/textlayoutorientation.md)
  Constants that describe the text layout orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutorientationprovider/layoutorientation)*