# canOverlapSourceViewRect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the popover can overlap its view rectangle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var canOverlapSourceViewRect: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL canOverlapSourceViewRect;
```

#### Discussion

Setting this property to [`true`](../../Swift/true.md) allows the popover to overlap the rectangle in the [`sourceRect`](./sourcerect.md) property when space is constrained. The default value of this property is false, which prevents the popover from overlapping the source rectangle.

## See Also

### Configuring the popover appearance
- [var popoverLayoutMargins: UIEdgeInsets](./popoverlayoutmargins.md)
  The margins that define the portion of the screen in which it is permissible to display the popover.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The color of the popover’s backdrop view.
- [var passthroughViews: [UIView]?](./passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.
- [var popoverBackgroundViewClass: (any UIPopoverBackgroundViewMethods.Type)?](./popoverbackgroundviewclass.md)
  The class to use for displaying the popover background content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/canoverlapsourceviewrect)*