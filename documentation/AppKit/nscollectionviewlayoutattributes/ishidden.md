# isHidden

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the element is hidden.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var isHidden: Bool { get set }
```

```objc
@property (getter=isHidden) BOOL hidden;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md). As an optimization, the collection view might not create the corresponding view when the value of this property is [`true`](../../Swift/true.md). Because there might not be a view, hidden elements do not participate in hit testing for the collection view.

## See Also

### Accessing the Layout Attributes
- [var frame: NSRect](./frame.md)
  The frame rectangle of the element.
- [var size: NSSize](./size.md)
  The size of the element.
- [var alpha: CGFloat](./alpha.md)
  The transparency of the element.
- [var zIndex: Int](./zindex.md)
  The element’s position on the z axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/ishidden)*