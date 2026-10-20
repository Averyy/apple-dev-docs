# alpha

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The transparency of the element.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var alpha: CGFloat { get set }
```

```objc
@property CGFloat alpha;
```

#### Discussion

Possible values are between `0.0` (fully transparent) and `1.0` (fully opaque). The default value is `1.0`.

Transparent items continue to participate in hit testing for the collection view.

## See Also

### Accessing the Layout Attributes
- [var frame: NSRect](./frame.md)
  The frame rectangle of the element.
- [var size: NSSize](./size.md)
  The size of the element.
- [var isHidden: Bool](./ishidden.md)
  A Boolean value indicating whether the element is hidden.
- [var zIndex: Int](./zindex.md)
  The element’s position on the z axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/alpha)*