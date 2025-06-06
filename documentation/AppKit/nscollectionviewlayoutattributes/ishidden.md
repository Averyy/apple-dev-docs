# isHidden

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the element is hidden.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var isHidden: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). As an optimization, the collection view might not create the corresponding view when the value of this property is [`true`](https://developer.apple.com/documentation/swift/true). Because there might not be a view, hidden elements do not participate in hit testing for the collection view.

## See Also

- [var frame: NSRect](nscollectionviewlayoutattributes/frame.md)
  The frame rectangle of the element.
- [var size: NSSize](nscollectionviewlayoutattributes/size.md)
  The size of the element.
- [var alpha: CGFloat](nscollectionviewlayoutattributes/alpha.md)
  The transparency of the element.
- [var zIndex: Int](nscollectionviewlayoutattributes/zindex.md)
  The element’s position on the z axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/ishidden)*