# frame

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The frame rectangle of the element.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var frame: NSRect { get set }
```

```objc
@property NSRect frame;
```

#### Discussion

The frame rectangle is measured in points and specified in the collection view’s coordinate system. Setting the value of this property also updates the value in the [`size`](./size.md) property.

## See Also

### Accessing the Layout Attributes
- [var size: NSSize](./size.md)
  The size of the element.
- [var alpha: CGFloat](./alpha.md)
  The transparency of the element.
- [var isHidden: Bool](./ishidden.md)
  A Boolean value indicating whether the element is hidden.
- [var zIndex: Int](./zindex.md)
  The element’s position on the z axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/frame)*