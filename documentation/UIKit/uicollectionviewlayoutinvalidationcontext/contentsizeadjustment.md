# contentSizeAdjustment

**Framework**: UIKit  
**Kind**: property

The delta value to be applied to the collection view’s content size.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentSizeAdjustment: CGSize { get set }
```

#### Discussion

Use this property to update the size of the collection view’s content area. The default value of this property is [`CGSizeZero`](https://developer.apple.com/documentation/CoreGraphics/CGSizeZero). Changing the value causes the collection view to add the specified height and width values to its [`contentSize`](uiscrollview/contentsize.md) property. Thus, positive values grow the content area and negative values shrink it.

## See Also

- [var contentOffsetAdjustment: CGPoint](uicollectionviewlayoutinvalidationcontext/contentoffsetadjustment.md)
  The delta value to be applied to the collection view’s content offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/contentsizeadjustment)*