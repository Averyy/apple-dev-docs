# size

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The size of the element.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var size: NSSize { get set }
```

```objc
@property NSSize size;
```

## Discussion

Setting the value of this property also updates the value in the [`frame`](./frame.md) property.

## See Also

### Accessing the Layout Attributes
- [var frame: NSRect](./frame.md)
  The frame rectangle of the element.
- [var alpha: CGFloat](./alpha.md)
  The transparency of the element.
- [var isHidden: Bool](./ishidden.md)
  A Boolean value indicating whether the element is hidden.
- [var zIndex: Int](./zindex.md)
  The element’s position on the z axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/size)*