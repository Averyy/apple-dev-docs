# zIndex

**Framework**: AppKit  
**Kind**: property

The element’s position on the z axis.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var zIndex: Int { get set }
```

#### Discussion

Use this property to specify the front-to-back ordering of items during layout. Items with higher index values appear on top of those with lower values. Items with the same value have an undetermined order.

The default value of this property is `0`.

## See Also

- [var frame: NSRect](nscollectionviewlayoutattributes/frame.md)
  The frame rectangle of the element.
- [var size: NSSize](nscollectionviewlayoutattributes/size.md)
  The size of the element.
- [var alpha: CGFloat](nscollectionviewlayoutattributes/alpha.md)
  The transparency of the element.
- [var isHidden: Bool](nscollectionviewlayoutattributes/ishidden.md)
  A Boolean value indicating whether the element is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/zindex)*