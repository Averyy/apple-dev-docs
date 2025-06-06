# layoutFrame

**Framework**: UIKit  
**Kind**: property

The layout guide’s frame in its owning view’s coordinate system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var layoutFrame: CGRect { get }
```

#### Discussion

The layout guide defines a rectangular space in its owning view’s coordinate system. This property contains a valid [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) value by the time its owning view’s [`layoutSubviews()`](uiview/layoutsubviews().md) method is called.

## See Also

- [func layoutSubviews()](uiview/layoutsubviews.md)
  Lays out subviews.
- [var identifier: String](uilayoutguide/identifier.md)
  A string used to identify the layout guide.
- [var owningView: UIView?](uilayoutguide/owningview.md)
  The view that owns this layout guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutguide/layoutframe)*