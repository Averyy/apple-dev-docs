# layoutFrame

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The layout guide’s frame in its owning view’s coordinate system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var layoutFrame: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect layoutFrame;
```

#### Discussion

The layout guide defines a rectangular space in its owning view’s coordinate system. This property contains a valid [`CGRect`](../../CoreFoundation/cgrect.md) value by the time its owning view’s [`layoutSubviews()`](../uiview/layoutsubviews%28%29.md) method is called.

## See Also

### Related Documentation
- [func layoutSubviews()](../uiview/layoutsubviews%28%29.md)
  Lays out subviews.
### Working with layout guides
- [var identifier: String](./identifier.md)
  A string used to identify the layout guide.
- [var owningView: UIView?](./owningview.md)
  The view that owns this layout guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutguide/layoutframe)*