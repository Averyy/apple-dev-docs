# contentOffsetAdjustment

**Framework**: UIKit  
**Kind**: property

The delta value to be applied to the collection view’s content offset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentOffsetAdjustment: CGPoint { get set }
```

#### Discussion

Use this property to update the content offset of the collection view. The default value of this property is [`CGPointZero`](https://developer.apple.com/documentation/CoreGraphics/CGPointZero). Changing the value causes the collection view to add the specified x and y values to its [`contentOffset`](uiscrollview/contentoffset.md) property. Thus, positive values increase the content offset and negative values decrease it.

## See Also

- [var contentSizeAdjustment: CGSize](uicollectionviewlayoutinvalidationcontext/contentsizeadjustment.md)
  The delta value to be applied to the collection view’s content size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/contentoffsetadjustment)*