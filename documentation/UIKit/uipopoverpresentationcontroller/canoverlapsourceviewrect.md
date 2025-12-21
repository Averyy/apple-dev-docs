# canOverlapSourceViewRect

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the popover can overlap its view rectangle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var canOverlapSourceViewRect: Bool { get set }
```

#### Discussion

Setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) allows the popover to overlap the rectangle in the [`sourceRect`](uipopoverpresentationcontroller/sourcerect.md) property when space is constrained. The default value of this property is false, which prevents the popover from overlapping the source rectangle.

## See Also

- [var popoverLayoutMargins: UIEdgeInsets](uipopoverpresentationcontroller/popoverlayoutmargins.md)
  The margins that define the portion of the screen in which it is permissible to display the popover.
- [var backgroundColor: UIColor?](uipopoverpresentationcontroller/backgroundcolor.md)
  The color of the popover’s backdrop view.
- [var passthroughViews: [UIView]?](uipopoverpresentationcontroller/passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.
- [var popoverBackgroundViewClass: (any UIPopoverBackgroundViewMethods.Type)?](uipopoverpresentationcontroller/popoverbackgroundviewclass.md)
  The class to use for displaying the popover background content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/canoverlapsourceviewrect)*