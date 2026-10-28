# owningView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view that owns this layout guide.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
weak var owningView: UIView? { get set }
```

```objc
@property (nonatomic, weak, nullable) UIView * owningView;
```

## Discussion

By default, this property is `nil`. To participate in Auto Layout, the layout guide must be added to a view by calling its [`addLayoutGuide(_:)`](../uiview/addlayoutguide%28_%29.md) method. Do not modify this property directly. Instead, use the view’s [`addLayoutGuide(_:)`](../uiview/addlayoutguide%28_%29.md) and [`removeLayoutGuide(_:)`](../uiview/removelayoutguide%28_%29.md) methods, which update this property as necessary.

## See Also

### Working with layout guides
- [var identifier: String](./identifier.md)
  A string used to identify the layout guide.
- [var layoutFrame: CGRect](./layoutframe.md)
  The layout guide’s frame in its owning view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutguide/owningview)*