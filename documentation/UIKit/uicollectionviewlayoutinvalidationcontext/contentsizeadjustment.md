# contentSizeAdjustment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delta value to be applied to the collection view’s content size.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var contentSizeAdjustment: CGSize { get set }
```

```objc
@property (nonatomic) CGSize contentSizeAdjustment;
```

#### Discussion

Use this property to update the size of the collection view’s content area. The default value of this property is [`CGSizeZero`](../../CoreGraphics/cgsizezero.md). Changing the value causes the collection view to add the specified height and width values to its [`contentSize`](../uiscrollview/contentsize.md) property. Thus, positive values grow the content area and negative values shrink it.

## See Also

### Invalidating the Content Area
- [var contentOffsetAdjustment: CGPoint](./contentoffsetadjustment.md)
  The delta value to be applied to the collection view’s content offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/contentsizeadjustment)*